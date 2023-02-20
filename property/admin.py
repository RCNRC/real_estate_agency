from django.contrib import admin
from property.models import Flat, Complaint, Owner



class MembershipInline(admin.TabularInline):
    model = Flat.owners.through
    raw_id_fields = ["owner"]


@admin.register(Flat)
class FlatAdmin(admin.ModelAdmin):
    search_fields = ('town','address', 'owner')
    readonly_fields = ["created_at"]
    list_display = ["address", "price", "new_building", "construction_year", "town", "owners_phonenumber", "owners_pure_phone"]
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
    list_display = ["owner", "owners_phonenumber", "owners_pure_phone"]
    readonly_fields = ["owner", "owners_phonenumber", "owners_pure_phone"]
    raw_id_fields = ["flats"]
