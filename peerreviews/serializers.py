from rest_framework import serializers
from models import Reviewer, Author, Submission


class ReviewerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reviewer
        fields = ('name', 'affiliation', 'email', 'bio', 'research', 'website', 'member_date', 'number_reviews')

    def create(self, validated_data):
        return Reviewer(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.naem)
        instance.affiliation = validated_data.get('affiliation', instance.affiliation)
        instance.email = validated_data.get('email', instance.email)
        instance.bio = validated_data.get('bio', instance.bio)
        instance.research = validated_data.get('research', instance.research)
        instance.website = validated_data.get('website', instance.website)
        instance.member_date = validated_data.get('member_date', instance.member_date)
        instance.number_reviews = validated_data.get('number_reviews', instance.number_reviews)
        instance.save()
        return instance

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('name','email')

class SubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Submission
        fields = ('title', 'venue', 'status', 'authors', 'reviewers',
                    'reviewdeadline', 'link', 'attachment')
