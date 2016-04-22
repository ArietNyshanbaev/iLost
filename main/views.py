﻿#importings
from django.shortcuts import render_to_response, redirect, get_object_or_404, render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Cardstick, Mail
from django.core.context_processors import csrf
from django.core.urlresolvers import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
#impoer of models 

def main(request):
	#initialize variables
	args={}
	args.update(csrf(request))
	return render(request, 'main/main.html',args)

def check_activation(request):
	#initialize variables
	args={}
	args.update(csrf(request))
	if request.POST:
		card_id = request.POST['idcode']
		card = Cardstick.objects.filter(card_id = card_id)
		if card.count() > 0:
			card = card[0]
			if card.activated == True:
				message = "Данная карта уже использована, попробуйте еще раз ..."
				args['message'] = message
				return render_to_response('main/check_activation.html',args)
			else:
				args['card_id'] = card.card_id
				message = "Пожалуйста завершите активацию карты."
				args['message'] = message
				return render_to_response('main/activate.html', args)
		else:
			message = "Данный код не действителен, попробуйте еще раз ..."
			args['message'] = message
			return render_to_response('main/check_activation.html',args)
	else:
		return redirect(reverse('main:main'))
	

def report(request):
	#initialize variables
	args={}
	args.update(csrf(request))
	if request.POST:
		card_id = request.POST['card_id']
		card = Cardstick.objects.filter(card_id = card_id)
		if card.count() > 0:
			card = card[0]
			if card.activated == True:
				message = "Пожалуйста свяжитесь с владельцем"
				info = Cardstick.objects.get(card_id = card_id)
				args['info'] = info
			else:
				message = "Данная карта еще не активирована"
		else:
			message = "Данный код не действителен, попробуйте еще раз ..."
		args['message'] = message
		return render_to_response('main/report.html',args)

	else:
		return redirect(reverse('main:main'))

def activate(request):
	#initialize variables
	args={}
	args.update(csrf(request))
	if request.POST:
		name = request.POST['name']
		email = request.POST['email']
		telephone = request.POST['telephone']
		card_id = request.POST['card_id']
		card = Cardstick.objects.get(card_id = card_id)
		card.name = name
		card.email = email
		card.telephone = telephone
		card.activated = True
		
		card.save()
		args["message"] = "Вы успешно активировали идентификатор. "

		return render_to_response('main/thanks_page.html', args)
	else:
		message = "Пожалуйста завершите активацию карты."
		args['message'] = message

	return render_to_response('main/activate.html',args)

def message(request):
	#initialize variables
	args={}
	args.update(csrf(request))
	if request.POST:
		name = request.POST['name']
		email = request.POST['email']
		subject = request.POST['subject']
		message = request.POST['message']
		mail = Mail.objects.create(name=name,email=email,title=subject,body=message)
		mail.save()
	return redirect(reverse('main:main'))

def signin(request):
	# redirect to main page authorized users
	if request.user.is_authenticated():
		return redirect(reverse("main:main"))
	# initialize variables
	args={}
	args.update(csrf(request))

	if request.POST:
		username = request.POST['username']
		password = request.POST['password']

		user = authenticate(username=username, password=password)

		if user is not None:
			if user.is_active:
				login(request, user)
				return redirect(reverse('main:main'))
		else:
			args['error_message'] = "Имя пользователя и пароль не совпадают, попробуйте еще раз. "
			return render(request, 'main/signin.html', args)
	else:
		return render(request, 'main/signin.html', args)

@login_required(login_url=reverse_lazy('main:main'))
def signout(request):

	logout(request)
	return redirect(request.META.get('HTTP_REFERER'))