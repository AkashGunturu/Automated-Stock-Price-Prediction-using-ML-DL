# Stock-Info (NSE Stock-Market Tracker)
Stock Info - a user-friendly web application created to monitor &amp; deliver trivial information regarding stocks and indices of National Stock Exchange (NSE) created using Django Framework & front-end developed using Tailwind CSS.
The data has be mainly sourced from NSE-India Website & Rediff Money using Web Scrappinh with the help of Python Package (Beautiful Soup) and the Charts are made with NPM package (Chart.js)

## **View of the Web Application**
>#### **Home Page of the Web Application**
<table>
  <tr>
    <td>NIFTY-50 Section</td>
    <td>Top Gainers & Losers</td>
  </tr>
  <tr>
    <td valign="middle"><img src="https://user-images.githubusercontent.com/76606642/155951108-e99517b1-5e00-40b0-bc66-f2be60f40e44.jpg"></td>
    <td valign="middle"><img src="https://user-images.githubusercontent.com/76606642/155951127-a43a762b-f979-4000-b88b-e32ff322b19e.jpg"></td>
  </tr>
</table>


>#### **Indiviual Pages for Stocks & Indices Info**
<table>
  <tr>
    <td>Indiviual Stock Section (Including Finacial Details)</td>
    <td>Indivual NSE Index Section</td>
  </tr>
  <tr>
    <td valign="middle"><img src="https://user-images.githubusercontent.com/76606642/155952259-1b265fa5-c85e-45a0-8c90-74c0ee94eb62.jpg"></td>
    <td valign="middle"><img src="https://user-images.githubusercontent.com/76606642/155952277-a727baa1-72c2-47ae-bd7f-c744572a43e0.jpg"></td>
  </tr>
 </table>


#### **NSE Indices Page**

>##### The page shows information regarding the NSE Indices including both Broad Market Indices & Sectoral Indices
<br>


![5](https://user-images.githubusercontent.com/76606642/155952696-be842a46-6164-49d4-9f16-c50c2ab0b5ab.jpg)


#### **The Financial News Page**

>##### The page shows information regarding the top-industry headlines locally & around the globe. The news is fetched using [NEWS API](https://newsapi.org/)

<table>
  <tr>
    <td>Top Headlines</td>
    <td>World News</td>
  </tr>
  <tr>
    <td valign="middle"><img src="https://user-images.githubusercontent.com/76606642/155954120-458cd453-7d23-428f-b04f-cda790a98ede.jpg"></td>
    <td valign="middle"><img src="https://user-images.githubusercontent.com/76606642/155954213-a4210e78-2418-4ee8-907d-24ad2702feff.png"></td>
  </tr>
 </table>
 
### **Auto Complete Stock Names**

>##### The feature to auto-complete the stock names is added to provide user-convenience using Java Script.


https://user-images.githubusercontent.com/76606642/155955129-f8093667-2c2a-4a62-8336-f00996fbc691.mp4





### Installation of Web Application of your PC:



- Install Python 3.8. 



- Install project dependencies using Conda Environment `conda install --file requirements.txt`.



- Run the commands `python manage.py makemigrations` and `python manage.py migrate` in the project directory to make and apply migrations.



- Run the command `python manage.py runserver` to run the web server.



- Open web browser and goto `127.0.0.1:8000` url to start using the web application.
