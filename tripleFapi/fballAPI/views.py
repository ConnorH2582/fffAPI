from django.shortcuts import render,redirect
from django.views.generic import View
from django.http import JsonResponse,Http404
import requests
import json

# class AllQuarterbackView(View):
#     def get(self, request, year):
#         
