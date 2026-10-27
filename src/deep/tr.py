# -*- coding: utf-8 -*-
# Derin içerik (Türkçe). Bloklar: h2, h3, p, ul, ol, note. İç bağlantılar: [[slug|metin]].
DEEP = {
 "toc": "Bu sayfada",
 "services": {

  # ------------------------------------------------------------------ MECHANICAL
  "mechanical-engineering": {
   "blocks": [
    ["h2", "Mekanik sistemlerinizin mühendislik desteğine ihtiyaç duyduğunu gösteren belirtiler"],
    ["p", "Pek çok fabrika ve ticari bina, yıllar içinde parça parça oluşturulmuş sistemlerle çalışır: bir yere yeni bir makine, bir yere ek bir fan, arızalanan kazanın yerine başka bir kazan konur. Maliyetler ortaya çıkana kadar bariz bir sorun görünmez. Aşağıdakilerden herhangi biri size tanıdık geliyorsa, yapılandırılmış bir mekanik inceleme çoğu zaman kendi masrafını çıkarır."],
    ["ul", [
      "Bir üretim hattı ayda birkaç kez, kimsenin tam olarak açıklayamadığı nedenlerle duruyor.",
      "Üretim miktarı aynı kalırken enerji faturaları sürekli artıyor.",
      "Havalandırma; ısıyı, tozu, dumanı veya nemi kabul edilebilir sınırlar içinde tutamıyor.",
      "Yeni ekipman satın alınmadan önce elektriğin, basınçlı havanın, suyun veya buharın bu ekipmanı karşılayıp karşılamadığı kontrol edilmedi.",
      "Çizimler sahadaki gerçek kurulumla artık örtüşmüyor; bu yüzden her onarım tahminle başlıyor."]],
    ["h2", "Bir mekanik projeyi nasıl yürütüyoruz"],
    ["p", "Kararların kanıtlara dayanması ve ekipman için para harcanmadan önce gözden geçirilebilmesi amacıyla işi aşamalar halinde yürütürüz."],
    ["ol", [
      "Brifing ve saha incelemesi. Neyin, ne miktarda ve hangi koşullarda üretileceği konusunda anlaşırız. Varsayımda bulunmak yerine sahayı ve mevcut ekipmanı ölçeriz.",
      "Konsept. Yön konusunda erken karar verebilmeniz için, altyapı ihtiyaçları ve yaklaşık maliyet aralığıyla birlikte iki veya üç yerleşim alternatifi sunarız.",
      "Temel tasarım. Isı yükleri, hava debileri, boru ve kanal ebatları, taşıyıcı yapılar ve ekipman şartnameleri; hepsi sizin de inceleyebileceğiniz hesaplarla desteklenir.",
      "Tedarikçi karşılaştırması. Teklifleri yalnızca fiyata göre değil, aynı esaslara göre karşılaştıran teknik bir tablo hazırlarız.",
      "Detay tasarım. Bir müteahhidin tahmin yürütmeden uygulayabileceği çizimler, metrajlar ve talimatlar hazırlanır.",
      "Denetim ve devreye alma. Kurulumu çizimlerle karşılaştırır, testlere tanıklık eder ve eksiksiz bir dokümantasyonu size teslim ederiz."]],
    ["h2", "Pahalı hataları önleyen hesaplar"],
    ["p", "Gereğinden büyük boyutlandırma, en sık yapılan ve en az fark edilen hatalardan biridir. Geniş bir güvenlik payıyla boyutlandırılmış bir ısıtma, havalandırma veya soğutma sistemi daha pahalıya satın alınır, kısmi yükte verimsiz çalışır ve çoğu zaman kontrol sorunları yaratır. Yetersiz boyutlandırma da en az onun kadar maliyetlidir; çünkü tesis, sürecin gerektirdiği koşulları koruyamaz. Sistemleri pratik kurallara göre değil, hesaplanmış yüklere göre boyutlandırırız:"],
    ["ul", [
      "Bina kabuğu, ekipman, aydınlatma ve insanlar yoluyla oluşan ısı kazançları ve kayıpları.",
      "Kullanıcılar için ve toz, solvent veya buhar gibi proses emisyonları için gerekli havalandırma havası.",
      "Gerçekte hangi pompa ve fanlara ihtiyaç duyulduğunu belirleyen boru ve kanallardaki basınç kayıpları.",
      "Kaçaklar için gerçekçi bir pay da içeren basınçlı hava talebi.",
      "Ekipman temelleri, platformlar ve boru mesnetleri için yapısal kontroller."]],
    ["h2", "Ekipman seçimi: fiyatın yanında nelere bakıyoruz"],
    ["p", "En ucuz teklif nadiren sahip olması en ucuz makinedir. Tedarikçileri karşılaştırırken bütün tabloya bakarız:"],
    ["ul", [
      "Ekipmanın yalnızca anma noktasındaki değil, gerçekten çalışacağı saatler boyunca sağladığı verimlilik.",
      "Arnavutluk'ta veya bölgede yedek parça ve yetkin teknisyen bulunabilirliği.",
      "Vinç, erişim ve duruş süresi dahil teslim süresi ve montaj koşulları.",
      "Gürültü, titreşim, kapladığı alan ve bakım erişimi.",
      "Garanti koşulları ve nelerin garanti dışında kaldığı.",
      "Enerji ve bakım dahil beş ila on yıllık toplam sahip olma maliyeti."]],
    ["h2", "Komple yenileme yapmadan enerji verimliliği"],
    ["p", "Çoğu tesis, her şeyi değiştirmeden enerji tüketimini azaltabilir. Tipik önlemler arasında basınçlı hava kaçaklarının giderilmesi, sıcak ve soğuk boruların yalıtılması, pompa ve fanlara değişken hızlı sürücülerin takılması, egzoz havasından ısı geri kazanımı ve yalnızca belirgin biçimde büyük kalmış veya ömrünü doldurmuş ekipmanın değiştirilmesi sayılabilir. Çalışmaya bir etütle başlarız: ana sistemlerin tüketimini temsil edici bir dönem boyunca ölçer, önlemleri geri ödeme süresine göre sıralar ve bu sırayla öneririz. Aynı projenin elektrik tarafı ise [[electrical-engineering|elektrik mühendisliği]] hizmetimizin kapsamındadır."],
    ["h2", "Başlamak için sizden neler istiyoruz"],
    ["ul", [
      "Ürünün veya sürecin kısa bir tanımı ve hedeflediğiniz üretim miktarı.",
      "Bina planları ya da sahanın fotoğrafları ve temel ölçüleri.",
      "Varsa etiket bilgileriyle birlikte mevcut ekipman listesi.",
      "Varsa son on iki aya ait enerji ve altyapı faturaları.",
      "Teslim tarihiniz ve yaklaşık bütçe aralığınız."]],
    ["h2", "Kaçınmanıza yardımcı olduğumuz hatalar"],
    ["ul", [
      "Saha ihtiyacı karşılayabilir mi diye bir altyapı etüdü yapılmadan ekipman satın almak.",
      "Başka bir ülkedeki tasarımı, yerel iklime, şebeke kalitesine ve mevcut servis olanaklarına uyarlamadan kopyalamak.",
      "Bakım erişimini unutmak; böylece her filtre değişimi için iskele kurulması gerekir.",
      "Devreye alma testlerini atlamak; böylece sorunlar ancak müteahhit sahadan ayrıldıktan sonra ortaya çıkar."]],
    ["p", "Proje daha büyük bir yatırımın parçasıysa, gerçekçi mühendislik maliyetlerine dayanan bir [[business-plan|iş planı]], tahminlere dayanan bir plana kıyasla bir bankayı çok daha fazla ikna edecektir."],
    ["h2", "Mevcut tesislerde modernizasyon ve bakım stratejisi"],
    ["p", "Her proje sıfırdan bir tesis kurmakla ilgili değildir. Çoğu zaman elde bir fabrika, bir otel veya bir depo vardır ve soru şudur: mevcut sistemi hangi sırayla ve hangi bütçeyle iyileştirmeliyiz? Bu durumda önce arızaların kayıtlarına, bakım geçmişine ve operatörlerin gözlemlerine bakarız. Sorunlu noktalar çoğu zaman az sayıdadır; tekrar eden bir rulman arızası, yetersiz soğutma kulesi veya dengesiz bir hava dağıtımı gibi. Bunları öncelik sırasına koyar, her müdahale için yaklaşık maliyet ve beklenen fayda tarif ederiz. Böylece yatırımı yıllara yayabilir, üretimi durdurmadan adım adım ilerleyebilirsiniz."],
    ["p", "Bakım tarafında da basit ve uygulanabilir bir yaklaşım öneririz: kritik ekipmanların listesi, her biri için kontrol periyodu, yedek parça stok seviyesi ve arıza halinde kimin aranacağı. Bu bilgiler tek sayfalık bir planda toplandığında, kendi teknisyenleriniz de sistemi daha rahat yönetebilir."],
   ],
   "faqs": [
    ["Fabrikaların yanı sıra binalar için de ısıtma, havalandırma ve soğutma tasarlıyor musunuz?", "Evet. Üretim salonları, depolar, ofisler, oteller ve diğer ticari binalar için yük hesabından ekipman seçimine ve uygulama denetimine kadar HVAC tasarımı yapıyoruz."],
    ["İmzalamadan önce bir tedarikçinin teklifini inceleyebilir misiniz?", "Evet. Teklif edilen ekipmanın hesaplanan ihtiyaçla uyumlu olup olmadığını, kapsamda eksik bir kalem bulunup bulunmadığını ve teklifin diğerleriyle ömür boyu maliyet açısından nasıl karşılaştığını kontrol ediyoruz."],
    ["Hangi standartlara göre tasarım yapıyorsunuz?", "Tanınmış Avrupa ve uluslararası mühendislik standartlarına ve projeniz için Arnavutluk'ta geçerli olan gerekliliklere göre çalışıyoruz. Geçerli standart setini her projenin başında sizinle teyit ederiz."],
    ["Çizimlerimiz kayıpsa yardımcı olabilir misiniz?", "Evet. Kurulumu yerinde inceliyor, uygulama sonrası (as-built) çizimleri hazırlıyor ve bunları her türlü iyileştirmenin temeli olarak kullanıyoruz."]
   ]
  },

  # ------------------------------------------------------------------ ELECTRICAL
  "electrical-engineering": {
   "blocks": [
    ["h2", "Elektrik tasarımı neden ayrı bir mühendislik çalışması gerektirir"],
    ["p", "Elektrik tesisatı, bir binada diğer tüm sistemlerin bağımlı olduğu tek sistemdir; aynı zamanda sahada en sık doğaçlama yapılan sistemdir. Biraz küçük seçilmiş bir kablo, yukarısındaki şalterle koordine edilmemiş bir sigorta ya da hiç ölçülmemiş bir topraklama sistemi yıllarca sorunsuz çalışabilir, sonra en kötü anda arıza verebilir. Tesisatı önceden tasarlamak, sonradan düzeltmekten daha ucuzdur."],
    ["h2", "Eksiksiz bir elektrik projesi neleri kapsar"],
    ["ul", [
      "Her devre ve bütün bina için büyüme payı da gözetilerek yapılan yük hesabı.",
      "Akım, gerilim düşümü ve arıza koşulları için kablo boyutlandırması.",
      "Kısa devre seviyeleri ve koruma koordinasyonu; böylece arıza, bütün sahayı değil, en yakın şalteri devre dışı bırakır.",
      "Net tek hat şemaları ve etiketlemeyle dağıtım panoları.",
      "Topraklama ve ekipotansiyel bağlantı; bina gerektiriyorsa yıldırımdan korunma.",
      "İşin gereğini karşılayan ve enerji tüketimini düşük tutan aydınlatma tasarımı.",
      "Makineler ve bina hizmetleri için PLC sistemleri dahil otomasyon ve kontrol."]],
    ["h2", "Güç faktörü, harmonikler ve gerçekte ödediğiniz fatura"],
    ["p", "Pek çok sanayi abonesi, düşük güç faktörü nedeniyle ya da elektronik yükler şebekeyi bozduğu için gerekenden fazla öder. Motorlar, kaynak makineleri ve sürücüler, dağıtım şirketinin bedel yansıtabileceği reaktif güç çeker. Değişken hızlı sürücüler ve doğrultucular kabloları ve transformatörleri ısıtan, hassas ekipmanı rahatsız eden harmonikler üretir. Pahalı herhangi bir ekipman önermeden önce bu etkileri ölçer, anlamlı olduğu yerde güç faktörü düzeltmesi boyutlandırır ve filtre gerekip gerekmediğini kontrol ederiz."],
    ["h2", "Güneş enerjisi (fotovoltaik) sistemleri: öz tüketime göre boyutlandırma"],
    ["p", "Fotovoltaik bir sistem, gün içinde aksi halde satın alacağınız elektriği karşıladığında en çok değer üretir. Bu yüzden çatı büyüklüğünden değil, tüketim profilinizden yola çıkarız. Etüt, farklı sistem büyüklüklerini karşılaştırır, üretimin ne kadarını kendinizin kullanacağını gösterir, geri ödeme süresini açıkça belirtilmiş varsayımlarla tahmin eder; çatı yapısını, gölgelenmeyi, kablo güzergâhlarını ve bağlantı noktasını da kontrol eder. Şebeke bağlantısı dağıtım operatörünün prosedürlerine göre ilerler ve sürecin gerektirdiği teknik dokümantasyonu biz hazırlarız. Belirli bir tasarruf vaat etmeyiz; çünkü bu, tarifelere, tüketime ve o dönemde yürürlükte olan kurallara bağlıdır."],
    ["h2", "Operatörlerin gerçekten bakım yapabileceği otomasyon"],
    ["p", "İyi bir otomasyon, kendi teknisyenlerinizin arıza teşhisi yapabileceği kadar sadedir. Bölgede bulunabilen kontrolörler, sensörler ve sürücüler belirler, mantığı sade bir dille belgelendirir ve kontrol panolarını erişilebilir test noktalarıyla tasarlarız. Makineleri bir tedarikçi programlayacaksa, sonucun sürecin ihtiyacıyla örtüşmesi için net bir fonksiyonel şartname yazarız."],
    ["h2", "Devreye almadan önce ölçümler ve testler"],
    ["p", "Bir tesisat devreye girmeden önce test edilmeli ve sonuçlar kayda geçirilmelidir. Projeye bağlı olarak bu; yalıtım direnci, süreklilik, toprak hatası döngü empedansı, topraklama elektrodu direnci, kaçak akım koruma cihazlarının açma süreleri ve doğru faz sırasını kapsar. Mevcut tesislerde, gevşek bağlantıları arıza vermeden önce bulmak için panolarda termal kameradan da yararlanabiliriz. Protokolleri size teslim ederiz; bir sigortacının veya müfettişin isteyeceği belgeler de bunlardır."],
    ["h2", "Başlamak için sizden neler istiyoruz"],
    ["ul", [
      "Bina planları veya sahanın ve ana yüklerinin tanımı.",
      "Güncel elektrik faturaları ve varsa yük profili.",
      "Güç değerleri ve etiket bilgileriyle makine listesi.",
      "Eskimiş olsa bile mevcut elektrik çizimleri.",
      "Önümüzdeki üç ila beş yıl içindeki genişleme planları."]],
    ["h2", "Düzelttiğimiz yaygın sorunlar"],
    ["ul", [
      "Dolu, etiketsiz ve genişletilmesi imkânsız panolar.",
      "Birkaç makine eklendikten sonra anma değerinin üzerinde yüklenen kablolar.",
      "Seçicilik olmaması; bu yüzden tek bir kısa devre bütün binayı karartır.",
      "Kurulmuş ama hiç ölçülmemiş topraklama.",
      "Yüke göre değil, çatıya göre boyutlandırılmış fotovoltaik sistemler."]],
    ["p", "Elektrik tasarımı çoğunlukla [[mechanical-engineering|mekanik tasarımla]] birlikte yürür; çünkü motorlar, ısıtma ve soğutma en büyük elektrik yükleridir. Bir tesisin ya da güneş enerjisi sisteminin yatırım gerekçesi de bir [[business-plan|iş planında]] ortaya konabilir. Yeni bir binada her iki disiplini koordine ederiz; böylece kablo güzergâhları ve teknik odalar çakışmaz."],
    ["note", "Tanınmış uluslararası ve Avrupa tesisat standartlarına ve projeniz için geçerli olan Arnavutluk makamlarının ve şebeke operatörünün gerekliliklerine göre tasarım yaparız. Nihai onaylar yetkili makamlarda kalır."],
   ],
   "faqs": [
    ["Yeni bir fabrikanın tesisatını sıfırdan tasarlayabilir misiniz?", "Evet. Süreçten ve makine listesinden yola çıkar, yükleri hesaplar, dağıtımı tasarlar; ihale ve inşaat için çizimleri ve şartnameleri hazırlarız."],
    ["Mevcut tesisatları test ediyor musunuz?", "Evet. Mevcut tesisatları ölçüp inceliyor, bulguları risk sırasına göre raporluyor ve tahmini maliyetiyle birlikte düzeltici öneriler sunuyoruz."],
    ["Güneş panellerinin işletmem için mantıklı olup olmadığını nasıl anlarım?", "Saatlik veya günlük tüketiminizi farklı sistem büyüklüklerinin beklenen üretimiyle karşılaştırır, ardından ne kadarını kendiniz tüketeceğinizi ve belirtilen varsayımlarla geri ödeme süresini gösteririz."],
    ["Elektrik faturamı düşürmeme yardımcı olabilir misiniz?", "Çoğu zaman evet. Tarife yapısına, güç faktörüne, pik talebe ve boşa giden tüketime bakar, önlemleri geri ödeme süresine göre sıralarız."]
   ]
  },

  # ------------------------------------------------------------------ BUSINESS PLAN
  "business-plan": {
   "blocks": [
    ["h2", "Bir iş planı gerçekte ne işe yarar"],
    ["p", "Bir iş planının iki okuyucusu vardır. Birincisi, borç verip vermeyeceğine, yatırım yapıp yapmayacağına ya da ortak olup olmayacağına karar verecek kişidir; pazarı anladığınızı ve rakamların birbirini tuttuğunu görmek ister. İkincisi sizsiniz: planı yazma süreci, her varsayımı kâğıt üzerinde sınamaya zorlar ve bu, kendi paranızla denemekten çok daha ucuzdur. Yalnızca bir formu doldurmak için hazırlanan plan genellikle her iki okuyucuyu da tatmin edemez."],
    ["h2", "Bankanın veya yatırımcının okuyacağı bir plana neler koyuyoruz"],
    ["ol", [
      "Yönetici özeti. Fırsatı, ihtiyaç duyduğunuz tutarı ve bunun ne için kullanılacağını anlatan tek sayfa.",
      "Pazar analizi. Müşterilerin kim olduğu, talebin ne kadar büyük ve ne kadar hızlı büyüdüğü, kimlerin bu talep için rekabet ettiği ve sizin nasıl farklılaştığınız.",
      "Teklif ve fiyatlandırma. Ne sattığınız, müşterilerin neden sizi seçeceği ve fiyatın maliyetle ve rakiplerle ilişkisi.",
      "Satış ve pazarlama planı. Müşterilerin sizi gerçekte nasıl duyacağı ve satın alacağı; gerçekçi dönüşüm varsayımlarıyla.",
      "Operasyon planı. Konum, ekipman, tedarikçiler, personel ve kapasite; her adım için zaman çizelgesiyle.",
      "Yönetim ve organizasyon. Kimin ne yaptığı ve planın belirli kişilere bağımlı olduğu noktalar.",
      "Finansal model. Yukarıdaki varsayımlardan türetilen gelir, maliyet, nakit akışı, finansman ve getiriler.",
      "Riskler ve senaryolar. Neyin ters gidebileceği, ne kadar olası olduğu ve bu durumda ne yapacağınız."]],
    ["h2", "Planları kazandıran da kaybettiren de varsayımlardır"],
    ["p", "Bir finansal modeldeki her rakam bir varsayıma dayanır: fiyat, hacim, maliyet, ödeme koşulları, tam kapasiteye ulaşma süresi. Okuyucu, sonucu en çok değiştiren varsayımlara en dikkatli bakar. Biz bunları tek bir yerde listeler, her birine bir kaynak veya gerekçeli bir dayanak verir ve değiştiklerinde sonucun nasıl değiştiğini gösteririz. Hangi beş varsayımın en önemli olduğunu açıkça söyleyen bir plan, pürüzsüz bir eğri sunan plandan daha inandırıcıdır."],
    ["h2", "Finansal model: içinde neler var"],
    ["ul", [
      "Ürün veya segment bazında gelir; ilk yıl aylık, sonraki yıllarda yıllık.",
      "Başabaş noktasının net görülmesi için ayrı gösterilen sabit ve değişken maliyetler.",
      "Zamanlamasıyla birlikte ekipman, işyeri ve işletme sermayesi yatırımı.",
      "Vergileri, kredi geri ödemelerini ve satış ile tahsilat arasındaki gecikmeyi içeren nakit akışı.",
      "Kredi verenlerin ilk baktığı borç servis karşılama oranı ve yatırımcılar için getiri.",
      "Temel, iyimser ve kötümser olmak üzere üç senaryo ve her birinin kısa açıklaması."]],
    ["p", "Model, Excel formatında ve açık formüllerle teslim edilir; böylece bir fiyatı veya hacmi değiştirip sonucu bize başvurmadan görebilirsiniz."],
    ["h2", "Mühendislik planı nerede güçlendirir"],
    ["p", "Pek çok plan, kimsenin kontrol etmediği maliyetlerde başarısız olur: ekipmanın gerçek fiyatı, bir tesisin ihtiyaç duyduğu altyapı, inşaatın aldığı süre. Ekibimizde mühendisler bulunduğu için, bir üretim veya gayrimenkul projesinin maliyeti teknik bir temelden çıkarılabilir. Ekipman ve montaj maliyetleri tahminden değil, [[mechanical-engineering|mekanik]] ve [[electrical-engineering|elektrik]] şartnamelerinden gelir. Bu da planı bir kredi verenin karşısında savunmayı kolaylaştırır."],
    ["h2", "Bir planla pazara girmek"],
    ["p", "Plan, Arnavutluk pazarına yurt dışından girmeye yönelikse, müşterilere nasıl ulaşılacağını, bir distribütörle mi yoksa yerel bir şirketle mi çalışılacağını ve hukuki yapının ne olacağını da kapsar. Bu sorular [[market-entry-partnerships|pazara giriş ve ortaklıklar]] ile [[company-formation-albania|şirket kuruluşu]] konularıyla bağlantılıdır; plan ile pratik adımların birbiriyle uyumlu olması için bunları birlikte ele alabiliriz."],
    ["h2", "Başlamak için sizden neler istiyoruz"],
    ["ul", [
      "Kaba da olsa iş fikrinin veya projenin tanımı.",
      "Elinizde bulunan her türlü rakam: teklifler, fiyatlar, geçmiş satışlar, maliyetler.",
      "Planın amacı: banka kredisi, yatırımcı, hibe, ortak ya da kendi kararınız.",
      "Biliniyorsa aradığınız finansman tutarı.",
      "Planın yazılması gereken dil."]],
    ["h2", "Kaçınmanıza yardımcı olduğumuz hatalar"],
    ["ul", [
      "Umulan bir sonucu tahmin gibi sunmak.",
      "İşletme sermayesini unutmak; böylece kârlı bir işletme nakitsiz kalır.",
      "Yalnızca tek bir senaryo kullanmak.",
      "Başlangıç ile tam kapasiteye ulaşma arasındaki süreyi göz ardı etmek.",
      "Asıl karar verici bir ortakken bankaya, ya da tersine, yazmak."]],
    ["h2", "Planın sonrası: izleme ve güncelleme"],
    ["p", "İş planı bir kez yazılıp rafa kaldırılacak bir belge olmamalıdır. İşletme başladıktan sonra gerçekleşen rakamları plandaki rakamlarla karşılaştırmak, sapmaların nedenini anlamanın ve gerekirse kararları zamanında düzeltmenin en kolay yoludur. Modeli bu amaçla kuruyoruz: gerçekleşen satışları ve maliyetleri girdiğinizde sapmayı görebilirsiniz. İsterseniz belirli aralıklarla birlikte gözden geçirme toplantıları da yapabiliriz."],
    ["note", "Hiçbir danışman bir kredinin, hibenin veya yatırımın onaylanacağını garanti edemez. Planı, kredi verenlerin ve yatırımcıların yaygın olarak uyguladığı ölçütleri karşılayacak ve her varsayım savunulabilecek şekilde hazırlarız."],
   ],
   "faqs": [
    ["İş planı ile fizibilite çalışması arasındaki fark nedir?", "Fizibilite çalışması, bir fikrin peşinden gitmeye değip değmediğini sorar. İş planı ise devam edeceğinizi varsayar ve bunun nasıl yapılacağını ortaya koyar. Fikir hâlâ belirsizse çoğu zaman kısa bir fizibilite kontrolüyle başlarız."],
    ["Kaç senaryo sunuyorsunuz?", "En az üç: temel durum, iyimser durum ve kötümser durum; aralarında değişen ana varsayımlarla birlikte."],
    ["Plan bir hibe başvurusu için kullanılabilir mi?", "Çoğu zaman evet, ancak hibe programlarının kendi formatları ve ölçütleri vardır. Hangi programı düşündüğünüzü söylerseniz yapıyı ona göre uyarlarız."],
    ["Finansal modeli kendim güncelleyebilecek miyim?", "Evet. Model Excel'de ve açık formüllerle teslim edilir; girdileri değiştirip sonuçları okuyabilmeniz için kısa bir anlatım da ekleriz."]
   ]
  },

  # ------------------------------------------------------------------ MARKET ENTRY
  "market-entry-partnerships": {
   "blocks": [
    ["h2", "Pazara girişlerin çoğu neden aslında bir ortak seçimi kararıdır"],
    ["p", "Yeni bir ülkeye giren şirket, nadiren ürünü kötü olduğu için başarısız olur. Başarısızlığın nedeni, ilk yerel ortağın hızlı bir şekilde, iyi geçen bir görüşmeye ve samimi bir tavsiyeye dayanarak seçilmesidir. Küçük bir pazarda etki daha büyüktür; çünkü seçilecek ortak sayısı azdır ve kötü bir uyumu değiştirmek daha zordur. Bizim işimiz bu seçimi bilinçli hale getirmektir."],
    ["h2", "Arnavutluk pazarına giriş yolları"],
    ["p", "Ortak aramadan önce hangi yolu istediğinize karar vermek yararlıdır. Her birinin maliyeti, kontrol düzeyi ve riski farklıdır."],
    ["ul", [
      "Distribütör. Yerel bir şirket sizden satın alır ve yeniden satar. Başlamak hızlı ve ucuzdur, ancak fiyat ve marka üzerindeki kontrolünüz azdır.",
      "Satış temsilcisi. Yerel bir kişi veya şirket müşteri bulur ve komisyon kazanır; faturayı siz doğrudan kesersiniz. Kontrol daha fazladır, ancak stoku ve kredi riskini siz taşırsınız.",
      "Ortak girişim (joint venture). Siz ve yerel bir şirket ortak bir işletme kurarsınız. Ürününüzü onların bilgisi ve ilişkileriyle birleştirir; özenle hazırlanmış bir sözleşme gerektirir.",
      "Kendi iştirakiniz veya şubeniz. Azami kontrol sağlar, ancak kurma ve işletmenin tüm maliyetini getirir. Talep kanıtlandıktan sonraki bir adım olması sık görülür.",
      "Fason üretim veya yerel montaj. Nakliye maliyetleri, tarifeler veya tedarik süreleri yerel üretimi cazip kıldığında tercih edilir."]],
    ["h2", "Ortakları nasıl buluyor ve eliyoruz"],
    ["ol", [
      "Brifing. Ürününüz, hedef müşterileriniz, umduğunuz hacimler ve bir ortaktan beklentileriniz.",
      "Pazar etüdü. Kimlerin hangi kanallardan satın aldığı ve benzer ürünleri halihazırda kimlerin sattığı.",
      "Uzun liste. Ağımızdan ve açık kaynaklardan, uygun görünen şirketler.",
      "Eleme. Şirketin gerçekte ne yaptığını, müşterilerini, doğrulanabildiği ölçüde mali durumunu ve tedarikçiler ile alıcılar nezdindeki itibarını kontrol ederiz.",
      "Kısa liste ve görüşmeler. Tanıştırmaları hazırlar, gerektiğinde iş kültürleri arasında tercümanlık yapar ve not tutarız.",
      "Koşullar. İlişkiyi yapılandırmanıza ve sözleşme maddelerini hazırlamanıza yardımcı oluruz."]],
    ["h2", "İyi bir ortaklık sözleşmesi neleri kapsar"],
    ["ul", [
      "Bölge ve münhasırlık olup olmadığı; ortak hedeflerini tutturamazsa ne olacağı.",
      "Asgari alım veya satış taahhütleri ve bunların nasıl gözden geçirileceği.",
      "Fiyatlandırma, indirimler, ödeme koşulları ve kredi riskini kimin taşıdığı.",
      "Markanızın, ticari markalarınızın ve pazarlama materyallerinin kullanımı.",
      "Servis, garanti ve yedek parça sorumlulukları.",
      "Süre, yenileme ve stok ile müşteri devrini de içeren net fesih kuralları.",
      "Gizlilik ve know-how'ınızın korunması."]],
    ["p", "Sözleşmeler lisanslı avukatlar tarafından hazırlanır ve incelenir. Biz ticari noktaları hazırlar ve anlaşmanın masada kararlaştırılanla örtüşmesi için ortak avukatlarla birlikte çalışırız."],
    ["h2", "Kültür ve iletişim"],
    ["p", "Arnavutluk'ta iş yapma biçimi çoğu zaman kişisel ilişkiler ve doğrudan konuşma üzerinden ilerler. Resmi prosedürlere alışkın yabancı şirketler bunu düzensizlik olarak algılayabilir; yerel ortaklar ise resmiyeti güvensizlik olarak okuyabilir. İki tarafı da anlayan ve yalnızca kelimeleri değil beklentileri de çevirebilen birinin bulunması zaman kazandırır ve daha sonra uyuşmazlık gibi görünecek yanlış anlamaları önler."],
    ["h2", "İyi bir ortağın ve kötü bir ortağın işaretleri"],
    ["ul", [
      "İyi: Hedeflediğiniz müşterilere zaten satış yapıyor ve bunu gösterebiliyor.",
      "İyi: Hedefleri taahhüt etmeye ve sözleşmeye yazmaya istekli.",
      "İyi: Kendi tedarikçileri ve müşterileri onu iyi anıyor.",
      "Kötü: Satış taahhüdü vermeden tüm ülke için münhasırlık istiyor.",
      "Kötü: Yüksek avans ödemeleri veya kontrol edemeyeceğiniz bir kredi talep ediyor.",
      "Kötü: Müşterilerinize nasıl ulaşacağını açıklayamıyor."]],
    ["h2", "Başlamak için sizden neler istiyoruz"],
    ["ul", [
      "Katalog veya şartnamelerle birlikte ürün ya da hizmet tanımı.",
      "Hedef müşterileriniz ve ulaşmayı umduğunuz hacimler veya ciro.",
      "Değerlendirdiğiniz yol ya da hangi yolu seçmeniz gerektiği sorusu.",
      "Pazardaki mevcut bağlantılarınız veya geçmiş girişimleriniz.",
      "Zaman çizelgeniz ve keşif aşaması için bütçeniz."]],
    ["h2", "İlgili destek"],
    ["p", "Bir pazara girmek genellikle bir ortaktan fazlasını gerektirir. [[business-plan|İş planı]] rakamları ortaya koyar, [[company-formation-albania|şirket kuruluşu]] gerekirse yerel bir tüzel kişilik oluşturmayı kapsar ve [[business-partnerships|profesyonel ağımız]] projeyi destekleyebilecek mühendislere, avukatlara ve danışmanlara erişim sağlar."],
    ["h2", "İlk görüşmeden önce hazırlık"],
    ["p", "Potansiyel bir ortakla ilk toplantıya girmeden önce kendi önceliklerinizi netleştirmek, görüşmenin verimini önemli ölçüde artırır. Neleri pazarlığa açık bıraktığınızı, hangi noktaların kesinlikle vazgeçilmez olduğunu ve karşı tarafın hangi bilgileri paylaşmasını beklediğinizi önceden yazın. Ürününüzün Arnavutluk koşullarına uyumu, gerekli sertifikalar veya ithalat gereklilikleri gibi teknik sorular da bu aşamada gündeme gelmelidir. Biz bu hazırlığı birlikte yapar, toplantıdan sonra da ortak bir özet çıkararak hangi konuların kararlaştırıldığını kayda geçiririz."],
   ],
   "faqs": [
    ["Arnavutluk'ta temsilcim veya distribütörüm olarak mı çalışıyorsunuz?", "Hayır. Uygun ortakları bulmanıza, kontrol etmenize ve onlarla görüşmenize, ayrıca ilişkiyi yapılandırmanıza yardımcı oluyoruz. Ortak sizin karşı tarafınız olur, biz değil."],
    ["Zaten bir ortağı olan ama memnun olmayan bir şirkete yardımcı olabilir misiniz?", "Evet. İlişkiyi gözden geçirebilir, neyin işlemediğini belirleyebilir ve yeniden müzakere etmenize veya alternatif aramanıza yardımcı olabiliriz."],
    ["Uygun bir ortak bulmak ne kadar sürer?", "Sektöre ve gerekliliklere bağlıdır. İlk kısa liste genellikle pazar etüdünden sonra mümkün olur, ardından görüşmeler yapılır. Başlangıçta size yazılı bir zaman çizelgesi veririz."],
    ["Hizmet yalnızca yabancı şirketler için mi?", "Hayır. Arnavut şirketleri de yabancı tedarikçiler, teknoloji ortakları ve distribütörler bulmak için bu hizmetten yararlanıyor."]
   ]
  },

  # ------------------------------------------------------------------ COMPANY FORMATION
  "company-formation-albania": {
   "blocks": [
    ["h2", "Doğru hukuki şekli seçmek"],
    ["p", "Hukuki şekil; kimin sorumlu olacağını, şirketin nasıl kaynak yaratabileceğini ve ne kadar idari yük taşıyacağını belirler. Küçük ve orta ölçekli işletmelerin çoğu için seçim, bir limited şirket (SH.P.K.) ile daha büyük veya karmaşık projeler için bir anonim şirket (SH.A.) arasındadır. Diğer seçenekler arasında şahıs işletmesi ve yabancı bir şirketin şubesi bulunur. Şube, ana şirketin bir parçasıdır ve ana şirketin sorumluluğunu sınırlamaz; birçok yatırımcının ayrı bir yerel şirketi tercih etmesinin nedeni budur."],
    ["ul", [
      "SH.P.K. Sınırlı sorumluluk ve basit bir yapı isteyen sahipler için yaygın bir tercih.",
      "SH.A. Çok sayıda ortağı olan veya hisse çıkararak sermaye toplamayı planlayan projeler için uygun.",
      "Şahıs işletmesi. Basit, ancak sahibi işletmeden kişisel olarak sorumludur.",
      "Yabancı şirket şubesi. Ana şirket doğrudan faaliyet göstermek istediğinde yararlı; yukarıda anlatılan sorumluluk sonuçlarıyla birlikte."]],
    ["h2", "Adım adım tescil süreci"],
    ["ol", [
      "Şekli, unvanı, faaliyet konusunu ve hisse yapısını belirleyin.",
      "Kuruluş belgelerini hazırlayın: ortakların ve yöneticilerin bilgilerini içeren esas sözleşme (statü) ve kuruluş belgesi.",
      "Ortakların ve yöneticilerin kimlik belgelerini sağlayın. Yabancılar için yurt dışında düzenlenen belgelerin genellikle apostil veya legalizasyonu ve yeminli tercümesi gerekir.",
      "Ulusal İşletme Merkezi'ne (QKB) tescil yaptırın. Tescille birlikte şirket, işletme kimlik numarasını (NUIS) alır.",
      "Şirket için bir banka hesabı açın ve seçilen şekil için gerekiyorsa sermayeyi yatırın.",
      "Vergi tescilini ve şirket çalışan istihdam edecekse işveren yükümlülükleri ile sosyal sigorta kaydını tamamlayın.",
      "Muhasebeyi ve düzenli bildirim ve ödemelerin takvimini kurun."]],
    ["h2", "Tescilden önce netleştirilmesi gereken sorular"],
    ["ul", [
      "Faaliyet konusu. Gerçekte yapacağınız işle örtüşmelidir; çünkü bazı faaliyetler başlamadan önce lisans veya izin gerektirir.",
      "Merkez adresi. Şirketin Arnavutluk'ta bir merkezi olmalıdır ve adres, resmi yazıları alabileceğiniz bir adres olmalıdır.",
      "Sahiplik ve kontrol. Arnavutluk kuralları gerçek faydalanıcı sahiplerin belirlenmesini gerektirir; bu nedenle yapı en baştan şeffaf olmalıdır.",
      "Yönetici. Şirketi kimin yöneteceği ve bu kişinin Arnavutluk'ta ikamet etmesi gerekip gerekmediği.",
      "Vergiler. Şirketin katma değer vergisine kaydolup olmayacağı ve ne zaman kaydolacağı faaliyetine ve beklenen cirosuna bağlıdır ve bir muhasebeciyle teyit edilmelidir."]],
    ["h2", "Yurt dışından tescil"],
    ["p", "Pek çok yabancı kurucu Arnavutluk'a gitmek zorunda olup olmadığını sorar. Bazı durumlarda süreç, bir temsilciye verilen vekâletname ile tamamlanabilir. Bunun için belgenin usulüne uygun hazırlanması, doğru makam önünde imzalanması ve legalize edilmesi gerekir; önceden planlanmazsa zaman alır. Başlangıçta sizin durumunuzda neyin mümkün olduğunu ve kendi ülkenizde hangi belgeleri hazırlamanız gerektiğini söyleriz."],
    ["h2", "Tescilden sonra: sık unutulan yükümlülükler"],
    ["ul", [
      "Sabit tarihleri olan düzenli vergi bildirimleri ve ödemeleri.",
      "Yıllık mali tablolar.",
      "Ortaklar, adresler veya yöneticiler değiştiğinde şirket sicilinin güncel tutulması.",
      "Personel için iş sözleşmeleri ve sosyal sigorta.",
      "Faaliyete bağlı, yenilenmesi gerekebilecek lisans ve izinler."]],
    ["p", "Faaliyetinizi bilen iyi bir muhasebeci, geç bildirimleri ve cezaları önleyerek kendi masrafını çıkarır. Ortak muhasebeciler tanıştırabiliriz; ayrıca şirket kuruluşunu [[business-plan|iş planı]] ile ve ilgili olduğunda [[real-estate-investment-albania|gayrimenkul alımı]] ile bağlantılandırırız; böylece hukuki yapı yatırıma uygun olur."],
    ["h2", "Gerçekçi bir zaman çizelgesi"],
    ["p", "Belgeler tamamlandıktan sonra tescil adımının kendisi hızlı olabilir. Gecikmeler genellikle başka yerlerden gelir: apostil ve yeminli tercüme gerektiren yurt dışı belgeler, yeni bir şirket için bankanın hesap açılış ve uyum kontrolleri ve düzenlemeye tabi faaliyetler için lisanslar. Başlangıçta, kontrol edebildiğiniz adımları edemediklerinizden ayıran bir takvim veririz; böylece açılış tarihi en hızlı adıma değil, en yavaş adıma göre belirlenir."],
    ["h2", "Başlamak için sizden neler istiyoruz"],
    ["ul", [
      "Şirketin ne yapacağı, iki üç cümleyle.",
      "Ortakların adları, uyrukları ve hisse payları.",
      "Şirketi kimin yöneteceği.",
      "Arnavutluk'ta bizzat bulunup bulunmayacağınız ya da bir temsilci aracılığıyla mı işlem yapacağınız.",
      "Beklenen başlangıç tarihiniz."]],
    ["note", "Bu hizmet hukuki veya vergi danışmanlığının yerini tutmaz. Hukuki ve vergisel konular ortak avukatlar ve muhasebecilerle yürütülür; kurallar değişir, bu yüzden imzalamadan önce her şey güncel gerekliliklere göre doğrulanır."],
   ],
   "faqs": [
    ["SH.P.K. ile SH.A. arasındaki fark nedir?", "SH.P.K., az sayıda ortağı olan küçük ve orta ölçekli şirketler için olağan şekildir. SH.A. ise daha büyük yapılar ve hisse yoluyla sermaye toplamak için tasarlanmıştır. Planlarınızı öğrendikten sonra bir şekil öneriyoruz."],
    ["Mülkiyetimi gizli tutabilir miyim?", "Arnavutluk kuralları faydalanıcı sahiplerin belirlenmesini ve kaydedilmesini gerektirir; dolayısıyla yapı şeffaf olmalıdır. Hangi bilgilerin kimlerin erişimine açılacağını size açıklıyoruz."],
    ["Muhasebeciye ihtiyacım var mı?", "Uygulamada evet. Küçük bir şirketin bile düzenli bildirimleri ve ödemeleri vardır ve hatalar cezalara yol açar. Ortak muhasebeciler tanıştırabiliriz."],
    ["Şirket tescil edildikten sonra yardımcı olabilir misiniz?", "Evet. Banka hesabı, ilk sözleşmeler, ortaklar ve iş planı konularında destek verebilir, sizi muhasebeciler ve avukatlarla buluşturabiliriz."]
   ]
  },

  # ------------------------------------------------------------------ PARTNERSHIPS
  "business-partnerships": {
   "blocks": [
    ["h2", "Bir ağ neden bir rehberden daha iyi çalışır"],
    ["p", "Bir rehber size isimlerden oluşan bir liste verir. Bir ağ ise, her birinin neyde iyi olduğunu bilen, onların çalışmasını görmüş ve projenize uyup uymadıklarını dürüstçe söyleyebilen birini verir. Ağımızı profile ve referanslara göre kuruyoruz; kişileri yalnızca gerçek bir proje ve uyacaklarına inanmak için bir neden olduğunda tanıştırıyoruz."],
    ["h2", "Eşleştirme nasıl yapılır"],
    ["ol", [
      "İhtiyacınızı anlatırsınız: bir beceri, bir ortak veya bir tedarikçi ve bunun için olduğu proje.",
      "Biz bunu bir profile çeviririz: önem taşıyan beceriler, deneyim, büyüklük ve diller.",
      "Ağdan ve gerekirse ağın dışından seçim yapar, referansları kontrol ederiz.",
      "İki veya üç uygun adayı, onları neden seçtiğimizin gerekçeleriyle birlikte tanıştırırız.",
      "Onlarla görüşürsünüz. İlk toplantıya katılabilir, not tutabilir ve kapsamın netleşmesine yardımcı olabiliriz.",
      "İlerlemeye karar verirseniz, işbirliği koşullarını yazılı hale getirmenize yardımcı oluruz."]],
    ["h2", "Ağda kimler var"],
    ["ul", [
      "Makine ve elektrik mühendisleri ile teknik uzmanlar.",
      "İş, finans ve yönetim danışmanları.",
      "Avukatlar, noterler ve muhasebeciler.",
      "Tedarikçiler, üreticiler ve distribütörler.",
      "Gayrimenkul uzmanları ve klinikler.",
      "Proje arayan yatırımcılar."]],
    ["p", "Her üye profil ve referanslar üzerinden değerlendirilir. Ağı sınırlı sayıda alanda odaklı tutarız; böylece bir tanıştırma her zaman projeyle ilgili olur ve asla bir listedeki herkese gönderilen toplu bir e-posta olmaz."],
    ["h2", "Müşteriler için: iyi bir tanıştırma size neyi kazandırır"],
    ["p", "Güvenilir bir alt yüklenici veya danışmanı kendi başınıza bulmak zaman alır ve yanlış seçimin maliyeti daha sonra ortaya çıkar. Kısa ve gerekçeli bir aday listesi aramanızı kısaltır; en baştan yapılan yazılı bir anlaşma ise belirsiz rollerden doğan uyuşmazlıklardan sizi korur. Sorunuz esas olarak yeni bir pazarda müşterilere veya tedarikçilere ulaşmaksa, [[market-entry-partnerships|pazara giriş ve ortaklıklar]] sayfasına bakabilirsiniz."],
    ["h2", "Profesyoneller için: nasıl başvurulur"],
    ["p", "Bağımsız profesyoneller ve küçük şirketler, çoğu zaman daha büyük projeler için gereken becerilere sahiptir ancak görünürlükleri yoktur. Durumunuz buysa, uzmanlık alanınızın kısa bir tanımı, almak istediğiniz proje türleri ve ulaşabileceğimiz bir iki referansla e-posta yoluyla başvurun. Her başvuruyu inceleriz. Katılmak bir satın alma değildir ve iş garantisi vermez. Bir talep profilinize uyduğunda sizi tanıştırırız."],
    ["h2", "Bir işbirliği sözleşmesi neleri söylemelidir"],
    ["ul", [
      "İşin kapsamı ve her bölümden kimin sorumlu olduğu.",
      "Fiyatın nasıl belirlendiği ve ne zaman ödendiği; değişikliklerin nasıl ele alındığı dahil.",
      "Süreler, kabul ölçütleri ve bunlar kaçırılırsa ne olacağı.",
      "Üretilen sonuçların, çizimlerin ve belgelerin mülkiyeti.",
      "Gizlilik ve müşteri bağlantılarının akıbeti.",
      "Her iki tarafın işbirliğini nasıl sonlandırabileceği."]],
    ["p", "Diğer profesyonellerle çalışmak, teknik bir ikinci görüş kadar basit ya da ortak bir ihale kadar kapsamlı olabilir. Teknik işler için [[mechanical-engineering|makine mühendisliği]] ve [[electrical-engineering|elektrik mühendisliği]] sayfalarına bakın; finansman gerektiren projelerde ise genellikle ilk adım bir [[business-plan|iş planıdır]]."],
    ["h2", "İnsanları buluşturduğumuz tipik durumlar"],
    ["ul", [
      "Bir üretici, bir tesisat için lisanslı bir elektrikçiye veya makine müteahhidine ihtiyaç duyuyor ve telefon rehberi yerine gerekçeli bir kısa liste istiyor.",
      "Yabancı bir şirket, kendi anlayacağı bir dilde birlikte çalışabilecek yerel bir muhasebeci ve bir avukat arıyor.",
      "Sermayesi olan bir yatırımcı, yetkin bir yerel işletmecisi olan bir proje arıyor.",
      "Küçük bir mühendislik firması daha büyük bir ihaleye katılmak istiyor ve kendisini tanıtacak bir ana yüklenici arıyor.",
      "Bir klinik, otel veya emlak acentesi, uluslararası müşteri yönlendiren ve koordinasyonu üstlenen güvenilir bir ortak istiyor."]],
    ["h2", "Ortak seçerken dikkat edilmesi gereken uyarı işaretleri"],
    ["p", "Bir ortağı bizim aracılığımızla da bulsanız, kendi başınıza da bulsanız, ciddiye alınması gereken birkaç uyarı işareti vardır:"],
    ["ul", [
      "Çok iyi görünen vaatler ve arayabileceğiniz hiçbir referansın bulunmaması.",
      "Koşulları, fiyatları veya sorumlulukları yazıya dökmeye isteksizlik.",
      "Her işi yaptığını söyleyen ama alanınızda yakın tarihli bir çalışma gösteremeyen şirket.",
      "Henüz hiçbir iş tanımlanmadan yüksek avans ödemesi yapmanız için baskı.",
      "Doğrulanamayan veya soru sorduğunuzda değişen iletişim bilgileri."]],
    ["h2", "Her iki tarafı nasıl koruyoruz"],
    ["ul", [
      "Yalnızca gerçek bir ihtiyaç ve gerekçeli bir uyum olduğunda tanıştırırız.",
      "Koşullar iş başlamadan önce yazılı olarak kararlaştırılır.",
      "Talep üzerine gizlilik sözleşmeleri imzalarız.",
      "Sonuç garanti etmeyiz ve karar vermeden önce bunu açıkça söyleriz."]],
    ["p", "Bir ortaklığın sağlıklı ilerlemesi için ilk ayda küçük bir deneme işi ile başlamak çoğu zaman en güvenli yoldur. Böylece iletişim hızını, teslim kalitesini ve fatura düzenini büyük bir taahhüde girmeden görürsünüz. Deneme iyi geçerse kapsamı aşamalı olarak genişletir, geçmezse zarar sınırlı kalır. Biz de bu aşamada isteyen taraflara toplantı notlarını tutarak ve beklentileri yazıya dökerek yardımcı oluruz."],
   ],
   "faqs": [
    ["Ağa katılmak bir bedel gerektirir mi?", "Başvuru ücretsizdir. Sizi bir müşteriyle tanıştırırsak, herhangi bir komisyon veya ücretin koşulları önceden yazılı olarak kararlaştırılır."],
    ["Üyelerin proje alacağını garanti ediyor musunuz?", "Hayır. Bir talep profillerine uyduğunda üyeleri tanıştırırız, ancak iş garantisi veremeyiz."],
    ["Ağı bir tedarikçi bulmak için kullanabilir miyim?", "Evet. İhtiyacınızı anlatın, biz ağın içinden veya dışından uygun adaylar önerelim."],
    ["Profesyonelleri nasıl kontrol ediyorsunuz?", "Profillerini, deneyimlerini ve referanslarını inceleriz. Düzenlemeye tabi meslekler için geçerli ruhsatlar bekleriz."]
   ]
  },

  # ------------------------------------------------------------------ DENTAL TOURISM
  "dental-tourism-albania": {
   "blocks": [
    ["h2", "Diş turizmi gerçekte neleri içerir"],
    ["p", "Diş tedavisi için seyahat etmek, tıbbi bir kararı bir yolculukla birleştirir. Tıbbi kısım tamamen diş hekimine aittir. Bizim payımıza ise etrafındaki her şey düşer: kontrol edilebilir klinikler bulmak, yazılı bir teklif almak, seyahat ve konaklamayı ayarlamak, randevularda tercümanlık yapmak ve klinik ile sizin aranızdaki koordinasyonu sürdürmek. İyi organize edilmiş bir seyahat, lojistik yerine tedaviye odaklanmanızı sağlar."],
    ["h2", "Süreç nasıl işler"],
    ["ol", [
      "Bize durumunuzu kısaca anlatır, varsa röntgenlerinizi veya önceki tedavi kayıtlarınızı gönderirsiniz.",
      "Ortak kliniklerden bunları incelemelerini, bir tedavi planı ve yazılı bir teklif sunmalarını isteriz.",
      "Teklifleri karşılaştırırsınız: nelerin dahil olduğu, kaç seans gerektiği, kliniğin neyi garanti ettiği ve ne tür ek maliyetler çıkabileceği.",
      "Siz seçtikten sonra seyahati planlarız: uçuşlar, otel, havalimanı transferleri ve ziyaret programı.",
      "Arnavutluk'ta isterseniz size eşlik edebilir ve randevularda tercümanlık yapabiliriz.",
      "Tedaviden sonra iletişimde kalır ve takip sorularınız için kliniğe ulaşmanıza yardımcı oluruz."]],
    ["h2", "Diş hekimi olmadan klinikleri nasıl karşılaştırırsınız"],
    ["p", "Klinik kaliteyi bir broşürden değerlendiremezsiniz, ancak kliniğin nasıl çalıştığını gösteren bazı noktaları kontrol edebilirsiniz:"],
    ["ul", [
      "Diş hekimlerinin ve kliniğin ruhsatlı olup olmadığı ve sizi kimin tedavi edeceğini söyleyip söylemedikleri.",
      "Teklifin yazılı ve kalem kalem olup olmadığı ve nelerin kapsam dışı olduğunu belirtip belirtmediği.",
      "Telefonda verilen bir fiyat yerine, plandan önce hangi görüntüleme ve teşhisin yapıldığı.",
      "Hangi malzeme ve markaların kullanıldığı ve ayrıntıları yazılı alıp almadığınız.",
      "Garantinin neyi kapsadığı, ne kadar süreyle geçerli olduğu ve geçerliliğini korumak için neler yapmanız gerektiği.",
      "Kliniğin komplikasyonları nasıl ele aldığı ve evinize döndükten sonra ona ulaşıp ulaşamayacağınız."]],
    ["h2", "Seyahati gerçekçi biçimde planlamak"],
    ["p", "Bazı tedaviler tek ziyaret gerektirir. Diğerleri, aralarında iyileşme süresi olan birkaç ziyaret gerektirir. Örneğin implant söz konusu olduğunda, aşamalar arasında ne kadar bekleneceğine diş hekimi karar verir ve çoğu durumda bu süre aylarla ölçülür; bu da iki ayrı seyahat anlamına gelebilir. Başlangıçta klinikten gerçekçi bir program isteyin ve gerekli görünenden daha fazla gün ayırın; böylece bir uçuşu yakalamak için tedaviyi kısaltmak zorunda kalmazsınız."],
    ["h2", "Karar vermeden önce sorulacak sorular"],
    ["ul", [
      "Tedavinin her aşamasını kim yapacak ve baştan sona aynı diş hekimi mi olacak?",
      "Daha ucuz veya daha az müdahaleci alternatifler var mı ve neden bu seçenek öneriliyor?",
      "Riskler nelerdir ve sonuç planlandığı gibi olmazsa ne olur?",
      "Kaç ziyaret gerekiyor ve her biri ne kadar sürüyor?",
      "Garanti nelerin dışında kalıyor?",
      "Döndükten sonra kime başvuracağım ve ne kadar hızlı yanıt alacağım?"]],
    ["h2", "Bu hizmeti kimler kullanıyor"],
    ["p", "Müşterilerimizin çoğu, Arnavutluk'ta tedavi olmak isteyen yurt dışında yaşayan kişilerdir; tedaviyi memleket ziyaretiyle birleştiren Arnavut diasporası üyeleri de bunlara dahildir. Güvenilir bir yerel koordinatöre ihtiyaç duyan asistans şirketlerine ve seyahat organizatörlerine de yardımcı oluyoruz. Seyahatiniz Arnavutluk'ta daha uzun bir kalışı kapsıyorsa, ekibimiz [[real-estate-investment-albania|gayrimenkul gezisi ve yatırımı]] gibi ilgili ihtiyaçlarda da destek verebilir."],
    ["h2", "Tedavi sonrası bakım ve takip"],
    ["p", "İyi bir tedavi, koltuktan kalktıktan sonra olanları da içerir. Seyahat etmeden önce bakım talimatlarını, kliniği aramanızı gerektiren belirtileri ve birinin ne kadar hızlı yanıt vereceğini bildiğinizden emin olun. Evinizdeki herhangi bir diş hekiminin tedavinizi sürdürebilmesi için tedavi kayıtlarınızın, röntgenlerinizin ve kullanılan malzemelerin kopyalarını saklayın. Uluslararası hastalarla çalışmak isteyen klinikler, oteller ve asistans şirketleri [[business-partnerships|profesyonel ağımıza]] başvurabilir."],
    ["ul", [
      "Bakım talimatlarını kendi dilinizde yazılı olarak isteyin.",
      "Bir şey ters giderse kiminle ve hangi kanaldan iletişime geçeceğinizi kararlaştırın.",
      "Döndükten sonra kendi diş hekiminizle bir kontrol randevusu planlayın."]],
    ["h2", "Başlamak için sizden neler istiyoruz"],
    ["ul", [
      "Ülkeniz, tercih ettiğiniz seyahat tarihleri ve ne kadar kalabileceğiniz.",
      "Düşündüğünüz tedavi veya çözmek istediğiniz sorun.",
      "Elinizde bulunan röntgenler, taramalar veya tedavi kayıtları.",
      "Yalnız mı yoksa refakatçilerle mi seyahat edeceğiniz.",
      "İletişim için tercih ettiğiniz dil."]],
    ["note", "Biz bir diş kliniği değiliz ve tıbbi tavsiye vermeyiz. Teşhis, tedavi planları ve fiyatlar diş hekimi tarafından belirlenir. Lütfen her tedaviyi kendi diş hekiminizle veya doktorunuzla da görüşün."],
   ],
   "faqs": [
    ["Yurt dışında diş tedavisi güvenli mi?", "Güvenlik ülkeye değil, kliniğe ve diş hekimine bağlıdır. Bu nedenle seyahat etmeden önce ruhsatları, yazılı teklifleri, malzemeleri, garantiyi ve takip düzenlemelerini kontrol etmenize yardımcı oluyoruz."],
    ["Kaç gün kalmayı planlamalıyım?", "Tedaviye bağlıdır. Klinik size gerçekçi bir program vermelidir; hiçbir şey aceleye gelmesin diye yedek günler eklemenizi öneriyoruz."],
    ["Otel ve ulaşımı ayarlayabilir misiniz?", "Evet. Otel, havalimanı transferleri ve yerel ulaşımı ayarlıyor, size eşlik edip ziyaretlerde tercümanlık yapabiliyoruz."],
    ["Eve döndükten sonra bir sorun yaşarsam ne olur?", "Karar vermeden önce kliniğe garanti ve takip düzenlemelerini soruyoruz; böylece ne bekleyeceğinizi bilirsiniz ve gerekirse kliniğe ulaşmanıza yardımcı oluruz."]
   ]
  },

  # ------------------------------------------------------------------ REAL ESTATE
  "real-estate-investment-albania": {
   "blocks": [
    ["h2", "Avans ödemesinden önce yapılan kontroller neden önemlidir"],
    ["p", "Gayrimenkul genellikle bir kişinin veya şirketin yaptığı en büyük alımdır ve Arnavutluk'ta bir mülkün geçmişi, ilanın gösterdiğinden daha karmaşık olabilir. Onlarca yıl boyunca değişen mülkiyet kuralları, kaçak yapılaşma, iade ve tazminat talepleri ile eksik kayıtlar, görünüşte birbirinin aynı iki dairenin çok farklı riskler taşıyabileceği anlamına gelir. Ödeme yapmadan önce yapılan kontroller, önledikleri sorunlara kıyasla çok az maliyetlidir."],
    ["h2", "Ortak avukatla organize ettiğimiz hukuki kontroller"],
    ["ul", [
      "Mülkiyet. Satıcının tapuda kayıtlı malik olduğu ve satış hakkına sahip olduğu; kayıtlı bilgilerin gösterilen mülkle örtüştüğü.",
      "Takyidatlar. İpotekler, hacizler, irtifak hakları, kira hakları ve mülk üzerinde kayıtlı her türlü talep veya uyuşmazlık.",
      "Kadastro verileri. Mülkün alanının, sınırlarının ve kadastro kaydının gerçeğe uygun olduğu.",
      "Yapı yasallığı. Yapı ruhsatı ve gerekiyorsa yapının kullanımına ilişkin belgeler. Kaçak yapılaşma geçmişi olan mülkler özel dikkat gerektirir.",
      "Arazi ve mülkiyet talepleri. Özellikle arazide, önceki süreçlerden kaynaklanan çakışan taleplerin bulunup bulunmadığı.",
      "Kimler satın alabilir. Yabancı alıcılara ilişkin kurallar mülk türüne göre, örneğin binalar ile tarım arazisi arasında farklılık gösterebilir ve taahhütte bulunmadan önce doğrulanır."]],
    ["h2", "Teknik inceleme"],
    ["p", "Bir mülk hukuken kusursuz, teknik olarak zayıf olabilir. Mühendislerimiz bir gezinin göstermediği şeyleri inceler ve size yaklaşık tadilat maliyetlerini içeren bir rapor verir; böylece fiyatı gerçek rakamlarla pazarlık edebilirsiniz."],
    ["ul", [
      "Yapı: çatlaklar, oturmalar, rutubet ile döşemelerin, çatıların ve cephelerin durumu.",
      "Elektrik tesisatı: pano, kablolama, topraklama ve öngörülen kullanım için kapasite.",
      "Sıhhi tesisat, ısıtma, soğutma ve havalandırma.",
      "Yalıtım, pencereler ve olası enerji maliyetleri.",
      "Ticari ve endüstriyel binalarda: döşeme yükleri, erişim, altyapı ve planlanan faaliyete uygunluk."]],
    ["h2", "Varsayımları görünür getiri analizi"],
    ["p", "Bir alım aynı zamanda bir yatırım kararıdır. Beklenen maliyetlerin ve gelirlerin basit bir modelini kurarız: fiyat, vergiler ve harçlar, tadilat, gerekirse mobilyalandırma, ardından kira, doluluk ve işletme maliyetleri. Varsayımlar yazılıdır; böylece onları değiştirebilirsiniz. Sonucu birden fazla senaryoda gösteririz ve getiri vaat etmeyiz. Daha büyük veya karmaşık projelerde aynı analiz eksiksiz bir [[business-plan|iş planına]] genişletilebilir."],
    ["h2", "Amaca göre seçim"],
    ["ul", [
      "Kendi kullanımınız için. Konum, erişim, hizmetler, yapı kalitesi ve mülkü işletmenin maliyeti.",
      "Uzun dönemli kiralama. Bölgedeki talep, kira seviyeleri, kiracı profili ve yönetim eforu.",
      "Turizm. Mevsimsellik, kısa süreli kiralamaya ilişkin düzenlemeler ve işletme maliyeti.",
      "Proje geliştirme. Arazi kullanım kuralları, izinler, altyapı, erişim ve mühendislik katkısının şart olduğu inşaat maliyeti."]],
    ["h2", "Fiyatın ötesindeki maliyetler"],
    ["p", "İlandaki fiyat, bir mülke sahip olmanın tam maliyeti olmaktan nadiren ibarettir. Karar vermeden önce aşağıdakilerin hepsi için bütçe ayırın:"],
    ["ul", [
      "Devir vergileri, noter masrafları ve tescil maliyetleri.",
      "Hukuki kontroller ve teknik inceleme.",
      "Tadilat, mobilyalandırma ve incelemenin ortaya çıkardığı onarımlar.",
      "Emlak vergileri ve bina bakım giderleri.",
      "Mülkü kiraya vermeyi planlıyorsanız yönetim, sigorta ve boş kalma dönemleri."]],
    ["h2", "Şirket üzerinden satın alma"],
    ["p", "Bazı yatırımcılar vergi, sorumluluk veya ticari nedenlerle bir şirket üzerinden satın alır. Bu karar alımdan önce verilmelidir; çünkü bir mülkün sonradan şirkete devri maliyet ve karmaşıklık ekleyebilir. Sizin için geçerliyse, bu hizmeti [[company-formation-albania|şirket kuruluşu]] ile birleştirebiliriz."],
    ["h2", "Başlamak için sizden neler istiyoruz"],
    ["ul", [
      "Amacınız: oturmak, kiralamak, turizm, proje geliştirme veya iş amaçlı kullanım.",
      "Tadilata ne kadar harcamayı planladığınız dahil bütçeniz.",
      "Tercih ettiğiniz şehirler veya bölgeler.",
      "Gezmek için Arnavutluk'ta olup olmayacağınız ya da yurt dışından yardıma ihtiyaç duyup duymadığınız.",
      "Bireysel olarak mı yoksa bir şirket aracılığıyla mı satın almayı düşündüğünüz."]],
    ["h2", "Gezmekten imzaya kadarki adımlar"],
    ["ol", [
      "Amacı ve bütçeyi belirleyin, ardından mülkleri seçip gezin.",
      "Kısa listedeki mülkler için belgeleri isteyin.",
      "Herhangi bir ödemeden önce hukuki kontrolleri ve teknik incelemeyi tamamlayın.",
      "Bulguları kullanarak fiyatı pazarlık edin.",
      "Sözleşme koşullarını avukatla birlikte kararlaştırın ve yasanın gerektirdiği şekilde imzalayın.",
      "Yeni malikin tescilini ve teslimi tamamlayın."]],
    ["note", "Bu hizmet hukuki veya mali danışmanlığın yerini tutmaz. Gayrimenkul hukuku ve vergiler değişir ve yatırım yapma kararı sizde kalır. Hukuki kontroller tamamlanana kadar hiçbir avans ödemesi yapılmamasını öneriyoruz."],
   ],
   "faqs": [
    ["Yabancılar Arnavutluk'ta gayrimenkul satın alabilir mi?", "Kurallar mülk türüne ve alıcıya bağlıdır. Özellikle araziye ilişkin durum, binalara ilişkin durumdan farklıdır. Siz herhangi bir ödeme yapmadan önce güncel kuralları bir avukatla doğruluyoruz."],
    ["Gayrimenkul satıyor musunuz?", "Hayır. Mülk bulmanıza, kontrol etmenize ve değerlendirmenize yardımcı oluyoruz. Satılık mülk tutmuyoruz; bu da tavsiyemizi bağımsız kılıyor."],
    ["Yatırım getirisi garanti ediyor musunuz?", "Hayır. Getiri vaadi değil, varsayımları görünür ve birden fazla senaryolu bir analiz hazırlıyoruz."],
    ["Satın aldıktan sonra tadilatta yardımcı olabilir misiniz?", "Evet. Mühendislerimiz tadilat şartnamesini hazırlayabilir, maliyetleri tahmin edebilir ve işleri denetleyebilir."]
   ]
  },
 }
}
