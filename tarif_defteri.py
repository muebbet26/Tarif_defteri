print('Kodyazar: Tugba Akan')
print('\n')      
print('Tarif defteri: Tarif defterinizin dijital hali')
print('Tariflerinizi tek bir yerde, kategorilerine göre saklayabilirsiniz.')
print('Yeni tarifler ekleyebilir, dilediğiniz kategorideki tarifleri görüntüleyebilirsiniz.')

#Tarifler şu adresten alındı: https://www.nefisyemektarifleri.com/

#Versiyon 1 : Kategoriler: Et yemekleri, Tavuk yemekleri, Sebze yemekleri
print('\n')
print('Yeni bir tarif eklemek istediğinizde, tarifin olduğu text dosyasını kodun çalışacağı klasöre koyun')
print('Kodu çalıştırdığınızda klasörde bulunan tüm text dosyalarını, yeni eklediğiniz dahil, okur.')
print('Jupyter notebook olarak çalıştırabilir')
print('ya da komut satırından py dosyasını çalıştırabilirsiniz.')

#Python 3
#Bu kodda kullanılan kavramlar şunlardır: 
#text dosyası yükleme ve metin madeciliği
#Nesne yönelimli programlama
#Exception handling

#Kategori sınıfı yaratılıyor
class Category(object):
    def __init__(self, ID, name, keywords):
        self.ID = ID
        self.name = name
        self.keywords = keywords

cate1 = Category( ID = 1, name='Et yemekleri', keywords=[' et ', ' et\n', ' eti ', ' eti\n', 'kıyma',  'kıyması', 'kıyması'])
cate2 = Category( ID = 2, name='Tavuk yemekleri', keywords= ['tavuk'])
cate3 = Category( ID = 3, name='Sebze yemekleri', keywords= ['patlıcan', 'semiz', 'lahana', 'kabak'] )

categories = [cate1, cate2, cate3 ]

#Tarif sınıfı yaratılıyor
class Recipe(object):
    def __init__(self,name, ingredients, categories):
        self.name = name
        self.ingredients = ingredients
        self.category = []
        self.setCategory(categories)
        
    #tarifin kategorisi bulunuyor
    def setCategory(self, categories):
        for cate in categories:
            for ingr in self.ingredients:
                if any(kw in ingr for kw in cate.keywords):
                    self.category.append(cate.name)
                    break

#eklemek istediginiz tarifi text dosyasına kaydedin
#en fazla 20 tarif olacagini varsaydik
recipes = []
for i in range(1,20):
    try:
        with open('tarif' + str(i) + '.txt', 'r') as f:
            new_recipe = f.readlines()
            rec = Recipe(name=new_recipe[0], ingredients = new_recipe[4::], categories = categories)
            recipes.append(rec)
    except IOError:
        #Dosyanın olup olmadıgını kontrol eder
        print( "Hata: dosya bulunamadi" )
    else:
        print( "Dosya basariyla yuklendi" )

#Kategorileri goruntule
#for item in categories:
#    print(item.name)

#Tarif defterindeki tüm yemek isimlerini ve kategorilerini goruntule
#for item in recipes:
#    print(item.name)
#    print(item.category)

#Sectigin bir kategorideki tarifleri goruntule
print('Goruntulemek istediginiz kategorinin numarasını yazın:')
for item in categories:
    print( str(item.ID) + ' for ' + item.name)
inp_cate_ID = input('')
for item in categories:
    if item.ID == int(inp_cate_ID):
        print(item.name)
        for item2 in recipes:
            for item3 in item2.category:
                if item3 == item.name:
                    print(item2.name)
