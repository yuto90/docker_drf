from rest_framework import viewsets, generics, pagination, response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from core.models import Todo

from todo import serializers


class TodoPagination(pagination.PageNumberPagination):
    """Get 2 Todo items in a page"""
    page_size = 2

    def get_paginated_response(self, data):
        return response.Response({
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'count': self.page.paginator.count,
            'total_pages': self.page.paginator.num_pages,
            'current_page': self.page.number,
            'results': data,
            'page_size': self.page_size,
            'range_first': (self.page.number * self.page_size) - (self.page_size) + 1,
            'range_last': min((self.page.number * self.page_size), self.page.paginator.count),
        })


class TodoViewSet(viewsets.ModelViewSet):
    """Handles creating, reading and updating todo items"""
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.TodoSerializer
    queryset = Todo.objects.order_by('-created_at')
    pagination_class = TodoPagination

    def perform_create(self, serializer):
        """Create a new Todo item"""
        serializer.save(user=self.request.user)