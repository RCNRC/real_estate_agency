from django.contrib import admin
from property.models import Flat, Complaint, Owner


class MembershipInline(admin.TabularInline):
    model = Flat.owners.through
    raw_id_fields = ["owner"]


@admin.register(Flat)
class FlatAdmin(admin.ModelAdmin):
    search_fields = ('town','address', 'owner')
    readonly_fields = ["created_at"]
    list_display = ["address", "price", "new_building", "construction_year", "town"]
    list_editable = ["new_building"]
    list_filter = ["new_building", "rooms_number", "has_balcony"]
    raw_id_fields = ["likes"]
    inlines = [
        MembershipInline
    ]


@admin.register(Complaint)
class ComplaintsAdmin(admin.ModelAdmin):
    raw_id_fields = ["user", "flat"]


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    list_display = ["name", "phonenumber", "pure_phone"]
    readonly_fields = ["name", "phonenumber", "pure_phone"]
    raw_id_fields = ["flats"]
