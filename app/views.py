from django.shortcuts import render
import razorpay


# Create your views here.
def home(request):
    
    return render(request,'home.html')
def second(request):
		

		return render(request,'donate.html')

def payment(request):
	if request.method == 'POST':
			name = request.POST.get('name')	 
			order_amount = request.POST.get('amount')*10000  
			order_currency = 'INR'             
			client = razorpay.Client(auth=('rzp_test_kE3jMsxyS0zoAa','0IeOjPC0bPk6HdNuKSO2o8Ov'))
			payment = client.order.create({'amount':amount,'currency':'INR','payment_capture':'1'}) 
	return render(request,'payment.html') 
# #    key-id ='rzp_test_kE3jMsxyS0zoAa'
# #    key_secret ='0IeOjPC0bPk6HdNuKSO2o8Ov'
   
       
 

	# client.order.create(amount=order_amount, currency=order_currency, receipt=order_receipt, notes=notes)
    
	

