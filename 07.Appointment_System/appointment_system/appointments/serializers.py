from rest_framework import serializers

from .models import Appointment

from accounts.models import Patient


class AppointmentSerializier(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__'


class AppointmentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ('date', 'reason', 'doctor_type')

    def create(self, validated_data):
        # import pdb; pdb.set_trace()
        patient = Patient.objects.get(user__pk=self.context['request'].user.id)
        validated_data['patient'] = patient
        validated_data['status'] = "P"
        return super(AppointmentCreateSerializer, self).create(validated_data)
