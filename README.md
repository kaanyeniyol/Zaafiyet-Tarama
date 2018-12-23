# Zaafiyet-Tarama

Bugün daha önceki staj günlerimde yaptığım nmap tabanlı tarama programını geliştirerek; Ip:port tarama, Ağa bağlı iplerin keşfi, 
ms17-010 eternalblue zafiyet tarayıcısı ve portları tarayarak alakalı güncel açıklıkları belirten nmap  tabanlı python kodu geliştirildi.

Subprocess, os, sys python modüllerini kullanarak kullanıcıdan bir ip veya ip aralığı isteyen progra-mımız kullanıcıdan istenildiği 
halde rapor oluşturulan bir sistem halinde geliştirilmiştir.

“ Taranacak ip adresi veya araligini gir : “ menusu altında "nmap -sS -sV -p- "+ip_adres + " -oX "+ip_adres +".xml" komutu ile ip_adres 
parametresinden anlaşılacağı gibi ip adresi girildikten sonra –sS, -sV, -p- ve –oX parametrelerini kullanarak zafiyet taraması 
gerçekleştirmektedir.

“ aginiza bagli ipler için : “ menusu altında kullanıcıdan istenen ip aralığı ile "nmap -sn "+ip_adres komutu ile –sn parametresi ile 
hızlı bir şekilde syn paket göndererek ağ üzerindeki canlı cihazlara ait ip taraması yapabilirsiniz.

“ms17-010 taramasi için” menusu altında genellikle windows 7 makinelerinde eternal-blue zafiyet taramasını 
os.system("nmap -p445 --script smb-vuln-ms17-010 "+ip_adres) komutu ile yapan eter-nal-blue zafiyetinin sadece port 445 aktif olduğu ve 
nmap hazır scripti bulunan  "smb-vuln-ms17-010 " ile zafiyet taraması gerçekleştirebilirsiniz.

“ Zafiyet taramasi için “ menusu altında ise ister bir ip üzerinde veya ip blokları üzerinde açık olan tüm portları tarayarak 
os.system("nmap --script vuln "+ip_adres) nmap komutunun vuln scripti ile zafiyet taraması yapmaktadır.

Programımız toplam 42 satır kod parçasından oluşmaktadır. Eğer belirtilen seçenekler dışarısında herhangi bir değer girildiğinde 
programımız tekrardan kullanıcıdan giriş isteyecek şekilde kodlanmış-tır. 
 
 
 
