# QR code Generator in python by Divyanshu Joshi
import qrcode
upi_id  = input("Enter your UPI id :")
#upi://pay?pa=UPI_ID&apn=NAME&am=amount&cii=CURRENCY&tn=MESSAGE

#Defining the payment URL based on the UPI ID and payment app
#you can modify these URLS based on the payment apps you want to support

paytm_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
phonepay_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
googlepay_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'

#Create QR codes for each payment App

phonepay_Qr = qrcode.make(phonepay_url)
paytm_Qr = qrcode.make(paytm_url)
googlepay_qr = qrcode.make(googlepay_url)

#save the QR code image file (optional)

phonepay_Qr.save('phonepay_qr.png')
paytm_Qr.save('paytm_qr.png')
googlepay_qr.save('googlepay_qr.png')

#Display the QR codes
phonepay_Qr.show()
paytm_Qr.show()
googlepay_qr.show()