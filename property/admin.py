from django.contrib import admin
from property.models import Flat, Complaint, Owner



class MembershipInline(admin.TabularInline):
    model = Flat.owners.through
    raw_id_fields = ["owner"]


class FlatAdmin(admin.ModelAdmin):
    search_fields = ('town','address', 'owner')
    readonly_fields = ["created_at"]
    list_display = ["address", "price", "new_building", "construction_year", "town", "owners_phonenumber", "owners_pure_phone"]
    list_editable = ["new_building"]
    list_filter = ["new_building", "rooms_number", "has_balcony"]
    raw_id_fields = ["users_liked"]
    inlines = [
        MembershipInline
    ]


class ComplaintsAdmin(admin.ModelAdmin):
    raw_id_fields = ["user", "flat"]


class OwnerAdmin(admin.ModelAdmin):
    raw_id_fields = ["flats"]


admin.site.register(Flat, FlatAdmin)
admin.site.register(Complaint, ComplaintsAdmin)
admin.site.register(Owner, OwnerAdmin)
