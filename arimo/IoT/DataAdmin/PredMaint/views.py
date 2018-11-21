from django.db.models import Prefetch

from rest_framework.authentication import \
    BasicAuthentication, RemoteUserAuthentication, SessionAuthentication, TokenAuthentication
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.renderers import CoreJSONRenderer, JSONRenderer
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet

from silk.profiling.profiler import silk_profile

from .filters import \
    EquipmentUniqueTypeGroupDataFieldProfileFilter, \
    EquipmentUniqueTypeGroupServiceConfigFilter, \
    BlueprintFilter, \
    EquipmentUniqueTypeGroupDataFieldBlueprintBenchmarkMetricProfileFilter, \
    EquipmentInstanceDailyRiskScoreFilter, \
    EquipmentProblemTypeFilter, \
    EquipmentProblemDiagnosisFilter, \
    AlertDiagnosisStatusFilter, \
    AlertFilter
from .models import \
    EquipmentUniqueTypeGroupDataFieldProfile, \
    EquipmentUniqueTypeGroupServiceConfig, \
    EquipmentUniqueTypeGroupMonitoredDataFieldConfig, \
    Blueprint, \
    EquipmentUniqueTypeGroupDataFieldBlueprintBenchmarkMetricProfile, \
    EquipmentInstanceDailyRiskScore, \
    EquipmentProblemType, \
    EquipmentProblemDiagnosis, \
    AlertDiagnosisStatus, \
    Alert
from .serializers import \
    EquipmentUniqueTypeGroupDataFieldProfileSerializer, \
    EquipmentUniqueTypeGroupServiceConfigSerializer, \
    BlueprintSerializer, \
    EquipmentUniqueTypeGroupDataFieldBlueprintBenchmarkMetricProfileSerializer, \
    EquipmentInstanceDailyRiskScoreSerializer, \
    EquipmentProblemTypeSerializer, \
    EquipmentProblemDiagnosisSerializer, \
    AlertDiagnosisStatusSerializer, \
    AlertSerializer

from ..base.models import EquipmentDataField


class EquipmentUniqueTypeGroupDataFieldProfileViewSet(ReadOnlyModelViewSet):
    """
    list:
    `GET` a filterable, paginated list of Equipment Unique Type Group Data Field Profiles

    retrieve:
    `GET` the Equipment Unique Type Group Data Field Profile specified by `id`
    """
    queryset = \
        EquipmentUniqueTypeGroupDataFieldProfile.objects \
        .select_related(
            'equipment_unique_type_group',
            'equipment_data_field', 'equipment_data_field__equipment_general_type', 'equipment_data_field__equipment_data_field_type')

    serializer_class = EquipmentUniqueTypeGroupDataFieldProfileSerializer

    authentication_classes = \
        BasicAuthentication, \
        RemoteUserAuthentication, \
        SessionAuthentication, \
        TokenAuthentication

    renderer_classes = \
        CoreJSONRenderer, \
        JSONRenderer

    permission_classes = IsAuthenticated,

    filter_class = EquipmentUniqueTypeGroupDataFieldProfileFilter

    ordering_fields = \
        'equipment_unique_type_group', \
        'equipment_data_field', \
        'to_date'

    ordering = \
        'equipment_unique_type_group', \
        'equipment_data_field', \
        '-to_date'

    pagination_class = LimitOffsetPagination

    @silk_profile(name='REST API: Equipment Unique Type Group Data Field Profiles')
    def list(self, request, *args, **kwargs):
        return super(EquipmentUniqueTypeGroupDataFieldProfileViewSet, self).list(request, *args, **kwargs)

    @silk_profile(name='REST API: Equipment Unique Type Group Data Field Profile')
    def retrieve(self, request, *args, **kwargs):
        return super(EquipmentUniqueTypeGroupDataFieldProfileViewSet, self).retrieve(request, *args, **kwargs)


class EquipmentUniqueTypeGroupServiceConfigViewSet(ReadOnlyModelViewSet):
    """
    list:
    `GET` a filterable, unpaginated list of Equipment Unique Type Group Service Configs

    retrieve:
    `GET` the Equipment Unique Type Group Service Config specified by `id`
    """
    queryset = \
        EquipmentUniqueTypeGroupServiceConfig.objects \
        .select_related(
            'equipment_unique_type_group') \
        .prefetch_related(
            Prefetch(
                lookup='equipment_unique_type_group_monitored_data_field_configs',
                queryset=
                    EquipmentUniqueTypeGroupMonitoredDataFieldConfig.objects
                    .select_related(
                        'monitored_equipment_data_field',
                        'monitored_equipment_data_field__equipment_general_type',
                        'monitored_equipment_data_field__equipment_data_field_type')
                    .prefetch_related(
                        Prefetch(
                            lookup='excluded_equipment_data_fields',
                            queryset=
                                EquipmentDataField.objects
                                .select_related(
                                    'equipment_general_type',
                                    'equipment_data_field_type')))),

            Prefetch(
                lookup='global_excluded_equipment_data_fields',
                queryset=
                    EquipmentDataField.objects
                    .select_related(
                        'equipment_general_type',
                        'equipment_data_field_type')))

    serializer_class = EquipmentUniqueTypeGroupServiceConfigSerializer

    authentication_classes = \
        BasicAuthentication, \
        RemoteUserAuthentication, \
        SessionAuthentication, \
        TokenAuthentication

    permission_classes = IsAuthenticated,

    filter_class = EquipmentUniqueTypeGroupServiceConfigFilter

    ordering_fields = \
        'active', \
        'equipment_unique_type_group'

    ordering = \
        '-active', \
        'equipment_unique_type_group'

    pagination_class = None

    renderer_classes = \
        CoreJSONRenderer, \
        JSONRenderer

    @silk_profile(name='REST API: Equipment Unique Type Group Service Configs')
    def list(self, request, *args, **kwargs):
        return super(EquipmentUniqueTypeGroupServiceConfigViewSet, self).list(request, *args, **kwargs)

    @silk_profile(name='REST API: Equipment Unique Type Group Service Config')
    def retrieve(self, request, *args, **kwargs):
        return super(EquipmentUniqueTypeGroupServiceConfigViewSet, self).retrieve(request, *args, **kwargs)


class BlueprintViewSet(ReadOnlyModelViewSet):
    """
    list:
    `GET` a filterable, paginated list of Blueprints

    retrieve:
    `GET` the Blueprint specified by `uuid`
    """
    queryset = \
        Blueprint.objects \
        .select_related(
            'equipment_unique_type_group')

    serializer_class = BlueprintSerializer

    authentication_classes = \
        BasicAuthentication, \
        RemoteUserAuthentication, \
        SessionAuthentication, \
        TokenAuthentication

    permission_classes = IsAuthenticated,

    lookup_field = 'uuid'

    lookup_url_kwarg = 'blueprint_uuid'

    renderer_classes = \
        CoreJSONRenderer, \
        JSONRenderer

    filter_class = BlueprintFilter

    ordering_fields = \
        'equipment_unique_type_group', \
        'trained_to_date', \
        'timestamp'

    ordering = \
        'equipment_unique_type_group', \
        '-trained_to_date', \
        '-timestamp'

    pagination_class = LimitOffsetPagination

    @silk_profile(name='REST API: Blueprints')
    def list(self, request, *args, **kwargs):
        return super(BlueprintViewSet, self).list(request, *args, **kwargs)

    @silk_profile(name='REST API: Blueprint')
    def retrieve(self, request, *args, **kwargs):
        return super(BlueprintViewSet, self).retrieve(request, *args, **kwargs)


class EquipmentUniqueTypeGroupDataFieldBlueprintBenchmarkMetricProfileViewSet(ReadOnlyModelViewSet):
    """
    list:
    `GET` a filterable, paginated list of Equipment Unique Type Group Data Field Blueprint Benchmark Metric Profiles

    retrieve:
    `GET` the Equipment Unique Type Group Data Field Blueprint Benchmark Metric Profile specified by `id`
    """
    queryset = \
        EquipmentUniqueTypeGroupDataFieldBlueprintBenchmarkMetricProfile.objects \
        .select_related(
            'equipment_unique_type_group',
            'equipment_data_field', 'equipment_data_field__equipment_general_type', 'equipment_data_field__equipment_data_field_type')

    serializer_class = EquipmentUniqueTypeGroupDataFieldBlueprintBenchmarkMetricProfileSerializer

    authentication_classes = \
        BasicAuthentication, \
        RemoteUserAuthentication, \
        SessionAuthentication, \
        TokenAuthentication

    permission_classes = IsAuthenticated,

    filter_class = EquipmentUniqueTypeGroupDataFieldBlueprintBenchmarkMetricProfileFilter

    ordering_fields = \
        'equipment_unique_type_group', \
        'equipment_data_field', \
        'trained_to_date'

    ordering = \
        'equipment_unique_type_group', \
        'equipment_data_field', \
        '-trained_to_date'

    pagination_class = LimitOffsetPagination

    renderer_classes = \
        CoreJSONRenderer, \
        JSONRenderer

    @silk_profile(name='REST API: Equipment Unique Type Group Data Field Blueprint Benchmark Metric Profiles')
    def list(self, request, *args, **kwargs):
        return super(EquipmentUniqueTypeGroupDataFieldBlueprintBenchmarkMetricProfileViewSet, self).list(request, *args, **kwargs)

    @silk_profile(name='REST API: Equipment Unique Type Group Data Field Blueprint Benchmark Metric Profile')
    def retrieve(self, request, *args, **kwargs):
        return super(EquipmentUniqueTypeGroupDataFieldBlueprintBenchmarkMetricProfileViewSet, self).retrieve(request, *args, **kwargs)


class EquipmentInstanceDailyRiskScoreViewSet(ReadOnlyModelViewSet):
    """
    list:
    `GET` a filterable, paginated list of Equipment Instance Daily Risk Scores

    retrieve:
    `GET` the Equipment Instance Daily Risk Score specified by `id`
    """
    queryset = \
        EquipmentInstanceDailyRiskScore.objects \
        .select_related(
            'equipment_unique_type_group',
            'equipment_instance')

    serializer_class = EquipmentInstanceDailyRiskScoreSerializer

    authentication_classes = \
        BasicAuthentication, \
        RemoteUserAuthentication, \
        SessionAuthentication, \
        TokenAuthentication

    permission_classes = IsAuthenticated,

    filter_class = EquipmentInstanceDailyRiskScoreFilter

    ordering_fields = \
        'equipment_unique_type_group', \
        'equipment_instance', \
        'risk_score_name', \
        'date'

    ordering = ()   # too numerous to order by default

    pagination_class = LimitOffsetPagination

    renderer_classes = \
        CoreJSONRenderer, \
        JSONRenderer

    @silk_profile(name='REST API: Equipment Instance Daily Risk Scores')
    def list(self, request, *args, **kwargs):
        return super(EquipmentInstanceDailyRiskScoreViewSet, self).list(request, *args, **kwargs)

    @silk_profile(name='REST API: Equipment Instance Daily Risk Score')
    def retrieve(self, request, *args, **kwargs):
        return super(EquipmentInstanceDailyRiskScoreViewSet, self).retrieve(request, *args, **kwargs)


class EquipmentProblemTypeViewSet(ModelViewSet):
    """
    list:
    `GET` a filterable, unpaginated list of Equipment Problem Types

    retrieve:
    `GET` the Equipment Problem Type specified by `name`

    create:
    `POST` a new Equipment Problem Type by `name`

    update:
    `PUT` updated data for the Equipment Problem Type specified by `name`

    partial_update:
    `PATCH` the Equipment Problem Type specified by `name`

    destroy:
    `DELETE` the Equipment Problem Type specified by `name`
    """
    queryset = EquipmentProblemType.objects.all()

    serializer_class = EquipmentProblemTypeSerializer

    authentication_classes = \
        BasicAuthentication, \
        RemoteUserAuthentication, \
        SessionAuthentication, \
        TokenAuthentication

    permission_classes = IsAuthenticated,

    lookup_field = 'name'

    lookup_url_kwarg = 'equipment_problem_type_name'

    renderer_classes = \
        CoreJSONRenderer, \
        JSONRenderer

    filter_class = EquipmentProblemTypeFilter

    ordering_fields = 'name',

    ordering = 'name',

    pagination_class = None

    @silk_profile(name='REST API: Equipment Problem Types')
    def list(self, request, *args, **kwargs):
        return super(EquipmentProblemTypeViewSet, self).list(request, *args, **kwargs)

    @silk_profile(name='REST API: Equipment Problem Type')
    def retrieve(self, request, *args, **kwargs):
        return super(EquipmentProblemTypeViewSet, self).retrieve(request, *args, **kwargs)


class EquipmentProblemDiagnosisViewSet(ModelViewSet):
    queryset = \
        EquipmentProblemDiagnosis.objects \
        .select_related(
            'equipment_instance') \
        .prefetch_related(
            'equipment_problem_types',
            Prefetch(
                lookup='alerts',
                queryset=
                    Alert.objects
                    .select_related(
                        'equipment_unique_type_group',
                        'equipment_instance',
                        'diagnosis_status')))

    serializer_class = EquipmentProblemDiagnosisSerializer

    authentication_classes = \
        BasicAuthentication, \
        RemoteUserAuthentication, \
        SessionAuthentication, \
        TokenAuthentication

    permission_classes = IsAuthenticated,

    renderer_classes = \
        CoreJSONRenderer, \
        JSONRenderer

    filter_class = EquipmentProblemDiagnosisFilter

    ordering_fields = \
        'ongoing', \
        'from_date', \
        'to_date', \
        'equipment_instance', \
        'dismissed'

    ordering = \
        '-ongoing', \
        '-from_date', \
        '-to_date', \
        'equipment_instance', \
        'dismissed'

    pagination_class = LimitOffsetPagination

    @silk_profile(name='REST API: Equipment Problem Diagnoses')
    def list(self, request, *args, **kwargs):
        return super(EquipmentProblemDiagnosisViewSet, self).list(request, *args, **kwargs)

    @silk_profile(name='REST API: Equipment Problem Diagnosis')
    def retrieve(self, request, *args, **kwargs):
        return super(EquipmentProblemDiagnosisViewSet, self).retrieve(request, *args, **kwargs)


class AlertDiagnosisStatusViewSet(ReadOnlyModelViewSet):
    """
    list:
    `GET` a filterable, unpaginated list of Alert Diagnosis Statuses

    retrieve:
    `GET` the Alert Diagnosis Status specified by `name`
    """
    queryset = AlertDiagnosisStatus.objects.all()

    serializer_class = AlertDiagnosisStatusSerializer

    authentication_classes = \
        BasicAuthentication, \
        RemoteUserAuthentication, \
        SessionAuthentication, \
        TokenAuthentication

    permission_classes = IsAuthenticatedOrReadOnly,

    lookup_field = 'name'

    lookup_url_kwarg = 'alert_diagnosis_status_name'

    renderer_classes = \
        CoreJSONRenderer, \
        JSONRenderer

    filter_class = AlertDiagnosisStatusFilter

    ordering_fields = 'index',

    ordering = 'index',

    pagination_class = None

    @silk_profile(name='REST API: Alert Diagnosis Statuses')
    def list(self, request, *args, **kwargs):
        return super(AlertDiagnosisStatusViewSet, self).list(request, *args, **kwargs)

    @silk_profile(name='REST API: Alert Diagnosis Status')
    def retrieve(self, request, *args, **kwargs):
        return super(AlertDiagnosisStatusViewSet, self).retrieve(request, *args, **kwargs)


class AlertViewSet(ModelViewSet):
    """
    list:
    `GET` a filterable, paginated list of Alerts

    retrieve:
    `GET` the Alert specified by `id`

    partial_update:
    `PATCH` the `diagnosis_status` of the Alert specified by `id`
    """
    queryset = \
        Alert.objects \
        .select_related(
            'equipment_unique_type_group',
            'equipment_instance',
            'diagnosis_status') \
        .prefetch_related(
            Prefetch(
                lookup='equipment_problem_diagnoses',
                queryset=
                    EquipmentProblemDiagnosis.objects
                    .select_related(
                        'equipment_instance')
                    .prefetch_related(
                        'equipment_problem_types')))

    serializer_class = AlertSerializer

    authentication_classes = \
        BasicAuthentication, \
        RemoteUserAuthentication, \
        SessionAuthentication, \
        TokenAuthentication

    permission_classes = \
        IsAuthenticated,

    renderer_classes = \
        CoreJSONRenderer, \
        JSONRenderer

    filter_class = AlertFilter

    ordering_fields = \
        'diagnosis_status', \
        'ongoing', \
        'risk_score_name', \
        'threshold', \
        'cumulative_excess_risk_score'

    ordering = \
        'diagnosis_status', \
        '-ongoing', \
        'risk_score_name', \
        '-threshold', \
        '-cumulative_excess_risk_score'

    pagination_class = LimitOffsetPagination

    @silk_profile(name='REST API: Alerts')
    def list(self, request, *args, **kwargs):
        return super(AlertViewSet, self).list(request, *args, **kwargs)

    @silk_profile(name='REST API: Alert')
    def retrieve(self, request, *args, **kwargs):
        return super(AlertViewSet, self).retrieve(request, *args, **kwargs)
