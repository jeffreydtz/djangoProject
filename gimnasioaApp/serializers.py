from rest_framework import serializers

from gimnasioaApp.models import User, Routine, Excercise, History


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'UserAge', 'UserWeight', 'UserHeight', 'UserGender', 'username',
                  'password']

    def create(self, validated_data):
        user = User.objects.create_user(
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email'],
            UserAge=validated_data['UserAge'],
            UserWeight=validated_data['UserWeight'],
            UserHeight=validated_data['UserHeight'],
            UserGender=validated_data['UserGender'],
            username=validated_data['username'],
            password=validated_data['password']
        )
        return user


class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Excercise
        fields = "__all__"


class RoutineSerializer(serializers.ModelSerializer):
    ejercicios = ExerciseSerializer(read_only=True, many=True)

    class Meta:
        model = Routine
        fields = "__all__"


class HistorySerializer(serializers.ModelSerializer):
    rutina = RoutineSerializer(read_only=True)

    class Meta:
        model = History
        fields = "__all__"
