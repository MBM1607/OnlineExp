from django.urls import path

import survey.dbSchema as dbSchema
import survey.views as views

app_name = "survey"

urlpatterns = [
    path("startSurvey/", views.startSurvey, name="startSurvey"),
    path("democraticOpinion/", views.democraticOpinion1, name="democraticOpinion1"),
    path("democraticOpinion2/", views.democraticOpinion2, name="democraticOpinion2"),
    path("newsAccuracyTask/", views.newsAccuracyTask, name="newsAccuracyTask"),
    path("waitingRoomNew/", views.waitingRoomNew, name="waitingRoomNew"),
    path("newsResponseInfo/", views.newsResponseInfo, name="newsResponseInfo"),
    path("newsResponse/", views.newsResponse, name="newsResponse"),
    path("quizTask/", views.quizTask, name= "quizTask" ),
    path("earnings/", views.earnings, name="earnings"),
    path("endOfSurvey/", views.endOfSurvey, name="endOfSurvey"),
    path("createDatabase/", dbSchema.createDatabase, name="createDatabase"),
    path("lastSeen/", views.lastSeen, name="lastSeen"),
    path("fillSchema/", dbSchema.fillSchema, name="fillSchema"),
    path("testingRoom/", views.testingRoom, name="testingRoom"),
    path("allotmentLogic2/", views.allotmentLogic2, name="allotmentLogic"),
    path("surveyRouter/", views.surveyRouter, name="surveyRouter"),
    path("timerNewsResponse/", views.timerNewsResponse, name="timerNewsResponse"),
    path("noSpotsAvailable/", views.noSpotsAvailable, name="noSpotsAvailable"),
]
