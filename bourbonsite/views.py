from django.shortcuts import render
from .models import Bourbon, Review
from .forms import ReviewForm
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from datetime import datetime
from django.contrib.auth.decorators import login_required


def bourbon_list(request):
    all_bourbons = Bourbon.objects.order_by('Bourbon')
    context = {'bourbon_list': all_bourbons}
    return render(request, 'bourbonsite/bourbon_list.html', context)


def bourbon_detail(request, BourbonID):
    bourbon = Bourbon.objects.filter(BourbonID=BourbonID)[0]
    reviews = Review.objects.order_by("-Pub_Date").filter(Bourbon_id=bourbon.id)[:9]
    chart = 'images/pie_charts/{}.png'.format(bourbon.BourbonID)
    bottle = 'images/bottles/{}.jpeg'.format(bourbon.BourbonID)
    form = ReviewForm()
    context = {'bourbon': bourbon, 'form': form, 'BourbonID': BourbonID, 'chart': chart, 'bottle': bottle, 'last10reviews':reviews}
    return render(request, 'bourbonsite/bourbon_detail.html', context)


def review_list(request):
    latest_review_list = Review.objects.order_by('-Pub_Date')
    context = {'latest_review_list': latest_review_list}
    return render(request, 'bourbonsite/review_list.html', context)


def review_detail(request, RatingID):
    review = Review.objects.filter(RatingID=RatingID)[0]
    return render(request, 'bourbonsite/review_detail.html', {'review': review})


def user_review_list(request, username=None):
    if not username:
        username = request.user.username
    latest_review_list = Review.objects.filter(User_Name=username).order_by('-Pub_Date')
    context = {'latest_review_list': latest_review_list, 'User_Name': username}
    return render(request, 'bourbonsite/user_review_list.html', context)


@login_required
def add_review(request, BourbonID):
    bourbon = Bourbon.objects.filter(BourbonID=BourbonID)[0]
    num_reviews = len(Review.objects.order_by('-Pub_Date'))
    form = ReviewForm(request.POST)
    if form.is_valid():
        rating = form.cleaned_data['Rating']
        comment = form.cleaned_data['Comment']
        user_name = request.user.username
        review = Review()
        review.RatingID = num_reviews + 1
        review.User_Name = user_name
        review.Bourbon = bourbon
        review.Comment = comment
        review.Pub_Date = datetime.now()
        review.Rating = rating
        review.save()
        print("Review Saved!!!")
        return HttpResponseRedirect(reverse('bourbonsite:bourbon_detail', args=(BourbonID,)))

    chart = 'images/pie_charts/{}.png'.format(bourbon.BourbonID)
    bottle = 'images/bottles/{}.jpeg'.format(bourbon.BourbonID)
    form = ReviewForm()
    context = {'bourbon': bourbon, 'form': form, 'BourbonID': BourbonID, 'chart': chart, 'bottle': bottle}
    return render(request, 'bourbonsite/bourbon_detail.html', context)