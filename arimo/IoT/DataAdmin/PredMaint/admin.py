from django.contrib.admin import ModelAdmin, site

from .forms import EquipmentProblemPeriodForm, AlertForm
from .models import Blueprint, EquipmentProblemType, EquipmentProblemPeriod, Alert


class BlueprintAdmin(ModelAdmin):
    list_display = \
        'equipment_general_type', \
        'equipment_unique_type_group', \
        'trained_to_date', \
        'timestamp', \
        'uuid', \
        'active'

    list_filter = \
        'equipment_general_type', \
        'equipment_unique_type_group', \
        'trained_to_date', \
        'timestamp', \
        'active'

    list_select_related = \
        'equipment_general_type', \
        'equipment_unique_type_group'

    show_full_result_count = False

    search_fields = \
        'equipment_general_type__name', \
        'equipment_unique_type_group__name', \
        'uuid'


site.register(
    Blueprint,
    admin_class=BlueprintAdmin)


class EquipmentProblemTypeAdmin(ModelAdmin):
    list_display = 'name',

    list_filter = 'name',

    show_full_result_count = False

    search_fields = 'name',


site.register(
    EquipmentProblemType,
    admin_class=EquipmentProblemTypeAdmin)


class EquipmentProblemPeriodAdmin(ModelAdmin):
    list_display = \
        'equipment_instance', \
        'from_date', \
        'to_date', \
        'equipment_problem_types', \
        'comments'

    list_filter = 'from_date', 'to_date'

    list_select_related = 'equipment_instance',

    show_full_result_count = False

    search_fields = 'equipment_instance__name',

    form = EquipmentProblemPeriodForm

    def equipment_problem_types(self, obj):
        return ', '.join(equipment_problem_type.name
                         for equipment_problem_type in obj.equipment_problem_types.all())


site.register(
    EquipmentProblemPeriod,
    admin_class=EquipmentProblemPeriodAdmin)


class AlertAdmin(ModelAdmin):
    list_display = \
        'equipment_general_type', \
        'equipment_unique_type_group', \
        'equipment_instance', \
        'risk_score_name', \
        'threshold', \
        'from_date', \
        'to_date', \
        'quantified_risk_degree', \
        'active'

    list_select_related = \
        'equipment_general_type', \
        'equipment_unique_type_group', \
        'equipment_instance'

    list_filter = \
        'equipment_general_type', \
        'equipment_unique_type_group', \
        'risk_score_name', \
        'threshold', \
        'from_date', \
        'to_date', \
        'active'

    show_full_result_count = False

    search_fields = \
        'equipment_general_type__name', \
        'equipment_unique_type_group__name', \
        'equipment_instance__name', \
        'risk_score_name'

    form = AlertForm


site.register(
    Alert,
    admin_class=AlertAdmin)
