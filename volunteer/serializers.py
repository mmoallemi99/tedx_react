from rest_framework import serializers
import smtplib,ssl


class SendMailFromSpeakerSerializer(serializers.Serializer):
    firstname = serializers.CharField(max_length=30, required=False)
    lastname = serializers.CharField(max_length=30, required=False)
    email = serializers.EmailField(required=False)
    phone_number = serializers.CharField(max_length=30, required=False)
    S_fullname = serializers.CharField(max_length=30, required=False)
    S_email = serializers.EmailField(required=False)
    S_reason = serializers.CharField(max_length=30, required=False)
    S_idea = serializers.CharField(max_length=30, required=False)
    number = serializers.CharField(max_length=30, required=False)
    verb = serializers.CharField(max_length=30, required=False)
    class Meta:
        fields = ('firstname', 'lastname', 'email', 'phone_number', 'S_fullname', 'S_email', 'S_reason', 'S_idea',
                  'number', 'verb')
    def validate(self, attrs):
        if attrs.get('verb') != 'introduce' and attrs.get('verb') != 'be':
            raise serializers.ValidationError({'verb': 'this should be equal to <be> or <introduce>'})
        return super().validate(attrs)

    def save(self, **kwargs):
        data = self.validated_data
        port = 465
        password = '123yekdose'
        context = ssl.create_default_context()
        smtp_server = 'smtp.gmail.com'
        sender = "my.ted.testmail@gmail.com"
        reciever = "Tedxuniversityofisfahan1@gmail.com"
        introduce_speaker = """/
                Subject: test for speaker volunteer's
                hi lovely organizer :)
                some one introduce a speaker
                first name: {}
                last name: {}
                email: {}
                phone number: {}
                full name of speaker: {}
                speaker's email: {}
                reason : {}
                idea : {}



                """.format(data.get('firstname'), data.get('lastname'), data.get('email'), data.get('phone_number'),
                           data.get('S_fullname'), data.get('S_email'), data.get('S_reason'), data.get('S_idea'))
        be_speaker = """

                Subject: test for speaker volunteer's
                hi lovely organizer :)
                some one sends request to be speaker

                full name of speaker: {}
                speaker's email: {}
                speaker's number: {}
                idea : {}


                """.format(data.get('S_full name'), data.get('S_email'), data.get('number'), data.get('S_idea'))
        message = None
        if data.get('verb') == 'introduce':
            message = introduce_speaker
        elif (data.get('verb') == 'be'):
            message = be_speaker
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender, password)
            server.sendmail(sender, reciever, message)