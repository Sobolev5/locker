import datetime
from datetime import timedelta

import shortuuid
from django.http import Http404
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import reverse
from django.urls import reverse

from encrypt.Encrypt import Encrypt
from encrypt.forms import AddRecordForm
from encrypt.forms import ShowRecordForm
from encrypt.models import Record


def add_record(request):

    if request.method == "POST":
        form = AddRecordForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data["text"]
            password = form.cleaned_data["password"]
            hours_locked = form.cleaned_data["hours_locked"]
            can_be_deleted = form.cleaned_data["can_be_deleted"]
            record = Record()
            record.text = text

            if hours_locked > 0:
                now = datetime.datetime.now()
                record.locked_till = now + timedelta(hours=hours_locked)

            record.text, record.iv = Encrypt.encrypt(text, password)
            record.can_be_deleted = can_be_deleted
            record.uuid = shortuuid.uuid()
            record.save()

            return HttpResponseRedirect(reverse("view_record", kwargs={"uuid": record.uuid}))
        else:
            raise Http404("Reload page and try again")
    else:
        form = AddRecordForm()
    return render(request, "encrypt/add_record.html", {"form": form})


def view_record(request, uuid):

    try:
        record = Record.objects.get(uuid=uuid)
    except:
        raise Http404

    now = datetime.datetime.now()
    if request.method == "POST":
        form = ShowRecordForm(request.POST)
        if form.is_valid():
            if record.locked_till:
                if record.locked_till > now:
                    raise Http404(f"Record locked till {record.locked_till}")

            decrypted_text = Encrypt.decrypt(record.text, record.iv, form.cleaned_data["password"])
            if decrypted_text:
                return render(request, "encrypt/view_record.html", {"record": record, "decrypted_text": decrypted_text, "decrypt": True})
            else:
                return render(request, "encrypt/view_record.html", {"record": record, "form": form, "decrypt": False, "invalid_password": True})
    else:
        form = ShowRecordForm()

    return render(request, "encrypt/view_record.html", {"record": record, "form": form, "decrypt": False, "now": now})


def delete_record(request, uuid, md5_key):

    try:
        record = Record.objects.get(uuid=uuid)
    except:
        raise Http404

    if record.md5_key_for_delete == md5_key and record.can_be_deleted:
        record.delete()
        return HttpResponse("Record deleted")
    else:
        raise Http404(f"Invalid link or record already deleted")
