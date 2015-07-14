from django.conf.urls import patterns, include, url
from django.contrib import admin
from fballAPI.views import AllQuarterbacksView, AllRunningbacksView, AllReceiversView, AllTightEndsView, AllKickersView, AllLinemenView, AllLinebackersView, AllDefensiveBacksView, AllPuntersView, QuarterbackView, RunningbackView, ReceiverView, TightEndView, KickerView, LinemanView, LinebackerView, DefensiveBackView, PunterView
from django.views.generic import View

urlpatterns = patterns('',

    # all positional offensive player stats in season
    url(r'^quarterbacks/(?P<year>20[0-2][0-9]+/)$', AllQuarterbacksView.as_view()),

    url(r'^runningbacks/(?P<year>20[0-2][0-9])/$', AllRunningbacksView.as_view()),

    url(r'^receivers/(?P<year>20[0-2][0-9])/$', AllReceiversView.as_view()),

    url(r'^tightends/(?P<year>20[0-2][0-9])/$', AllTightEndsView.as_view()),

    url(r'^kickers/(?P<year>20[0-2][0-9])/$', AllKickersView.as_view()),

    # all positional defensive player stats in season
    url(r'^linemen/(?P<year>20[0-2][0-9])/$', AllLinemenView.as_view()),

    url(r'^linebackers/(?P<year>20[0-2][0-9])/$', AllLinebackersView.as_view()),

    url(r'^defensivebacks/(?P<year>20[0-2][0-9])/$', AllDefensiveBacksView.as_view()),

    url(r'^punters/(?P<year>20[0-2][0-9])/$', AllPuntersView.as_view()),

    # individual offensive players by position, by game, in season
    url(r'^quarterbacks/(?P<year>20[0-2][0-9])/(?P<name_slug>[a-z_-]+)$', QuarterbackView.as_view()),

    url(r'^runningbacks/(?P<year>20[0-2][0-9])/(?P<name_slug>[a-z_-]+)$', RunningbackView.as_view()),

    url(r'^receivers/(?P<year>20[0-2][0-9])/(?P<name_slug>[a-z_-]+)$', ReceiverView.as_view()),

    url(r'^tightends/(?P<year>20[0-2][0-9])/(?P<name_slug>[a-z_-]+)$', TightEndView.as_view()),

    url(r'^kickers/(?P<year>20[0-2][0-9])/(?P<name_slug>[a-z_-]+)$', KickerView.as_view()),

    # individual defensive player stats by position, by game in season
    url(r'^linemen/(?P<year>20[0-2][0-9])/(?P<name_slug>[a-z_-]+)$', LinemanView.as_view()),

    url(r'^linebackers/(?P<year>20[0-2][0-9])/(?P<name_slug>[a-z_-]+)$', LinebackerView.as_view()),

    url(r'^defensivebacks/(?P<year>20[0-2][0-9])/(?P<name_slug>[a-z_-]+)$', DefensiveBackView.as_view()),

    url(r'^punters/(?P<year>20[0-2][0-9])/(?P<name_slug>[a-z_-]+)$', PunterView.as_view()),

)
