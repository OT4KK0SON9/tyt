#!/bin/sh

toilet -F metal "TOOLSV1"
echo "                 OtakKosong<="

clear

echo "______________________________"

echo " "
toilet -F metal "TOOLSV1"
echo "                 OtakKosong<=" | lolcat

echo " "

echo "______________________________"

echo "1.SPAM OTP"
echo "______________________________"
echo "2.Termux Tampilan Selamat Datang Wkwk"
echo "______________________________"
echo "3.Pelacak IP"
echo "______________________________"
echo "4.Cek Status Website"
echo "______________________________"
echo "0.Tunggu Update Selanjut Nya Karena Ini Masih Dalam Pemgembangan"
echo "______________________________"
echo "999.Keluar"
echo "______________________________"
read -p "PILIH > " YA

if [ $YA = 1 ]
then
echo "TUNGGU SEBENTAR..."
sleep 2.1s
git clone https://github.com/OT4KK0SON9/error
cd error
bash install.sh
ls
fi

if [ $YA = 2 ]
then
echo "TUNGGU SEBENTAR..."
sleep 2.7s
git clone https://github.com/OT4KK0SON9/TermuxSelamatDatang
cd TermuxSelamatDatang
bash install.sh
exit
fi

if [ $YA = 3 ]
then
echo "TUNGGU SEBENTAR..."
sleep 2.7s
python3 ipicker
exit
fi

if [ $YA = 4 ]
then
echo "TUNGGU SEBENTAR..."
sleep 2.7s
python3 y.py
exit
fi


if [ $YA = 0 ]
then
echo "TUNGGU SEBENTAR..."
echo "TUNGGU AJA UPDATE NYA SUBSCRIBE YUTUP GW SUPAYA TAU"
exit
fi

if [ $YA = 999 ]
then
echo "TUNGGU SEBENTAR..."
exit
else
  sleep 2
  echo "Jangan Ngasal Bang"
  bash apacoba.sh
  fi
