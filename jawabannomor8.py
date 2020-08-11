from bs4 import BeautifulSoup
import requests

def main():
    main_url = "http://academy.babastudio.com"
    r1 = requests.get(main_url)
    soup = BeautifulSoup(r1.text, 'html.parser')
    r1_link_array = soup.find_all('a') # melakukan list untuk mendapatkan link halaman login dari scraping homepage

    # Bagian ini seharusnya diisi bagaimana mendapatkan halaman login. Mengingat waktu terbatas, maka
    # saya lihat aja halaman web aslinya, karena lebih cepat daripada melakukan try-except.
    # Dari melihat website langsung, didapat url login adalah https://academy.babastudio.com/login.

    # Ini saya dapatkan dari penjelasan diatas.
    login_url = "https://academy.babastudio.com/login"
    r2 = requests.get(login_url)
    soup = BeautifulSoup(r2.text, 'html.parser')
    
    # Bagian dari login biasanya berupa form dengan method POST. Maka kita ambil data dengan filter form.
    r2_form_array = soup.find_all('form')

    # Output dari r2_form_array menunjukkan semua tag didalam form. Ada beberapa class disitu.
    # Jika kita tidak bisa mengakses halaman secara manual, maka perlu beberapa mekanisme.
    # Namun karena kita bisa mengakses halaman login secara manual dan kita tahu bahwa untuk
    # login diperlukan email dan password, maka setelah dibandingkan dengan output r2_form_array
    # akan diketahui bahwa input untuk authentikasi login menggunakan class form-signup.

    r2x_form_array = soup.find_all('form', class_="form-signup")
    
    # Dari data r2x_form_array, kita bisa menggunaka regex untuk mengekstrak value. Namun karena
    # sedikit, melihat output secara manual sudah bisa kita dapatkan data sbb:
    # url = 'https://academy.babastudio.com/login-post'
    # _token = 'DTbhuDwYYoief5OtITNnfZKjwckej1ZJpL0vnpzq'
    # tenant_id = '1'
    # log = "LOG_LOGIN"

    # Kita punya data email = 'academy.babastudio@tester.com' dan password = '12345678'.

    auth_url = 'https://academy.babastudio.com/login-post'
    mydata = {'_token':'DTbhuDwYYoief5OtITNnfZKjwckej1ZJpL0vnpzq', 'tenant_id':'1', 'log':'LOG_LOGIN', 'email':'academy.babastudio@tester.com', 'password':'12345678'}

    target_page = requests.post(auth_url, data = mydata)
    # Ini data yang bisa diolah.
    print(target_page.text) 

if __name__=="__main__":
    main()
