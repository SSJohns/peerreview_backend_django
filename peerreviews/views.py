from django.shortcuts import render
from rest_framework import viewsets
from models import Reviewer, Author, Submission
from serializers import ReviewerSerializer

# Create your views here.
def post_list(request):
    return render(request, 'peerreviews/test.html', {})


class ReviewerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows reviewers to be CRUDed.
    """
    queryset = Reviewer.objects.all()
    serializer_class = ReviewerSerializer

@api_view(['GET', 'POST'])
def reviewer_list(request):
    """
    List all snippets, or create a new snippet.
    """
    if request.method == 'GET':
        reviewers = Reviewer.objects.all()
        serializer = ReviewerSerializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ReviewerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AuthorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows reviewers to be CRUDed.
    """
    queryset = Reviewer.objects.all()
    serializer_class = ReviewerSerializer

@api_view(['GET', 'POST'])
def author_list(request):
    """
    List all snippets, or create a new snippet.
    """
    if request.method == 'GET':
        reviewers = Author.objects.all()
        serializer = AuthorSerializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = AuthorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SubmissionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows reviewers to be CRUDed.
    """
    queryset = Submission.objects.all()
    serializer_class = ReviewerSerializer

@api_view(['GET', 'POST'])
def submission_list(request):
    """
    List all snippets, or create a new snippet.
    """
    if request.method == 'GET':
        reviewers = Submission.objects.all()
        serializer = SubmissionSerializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = SubmissionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
