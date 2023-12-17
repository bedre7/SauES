# SauES

## 💻 Online Demo

You can play around with the online demo [here](https://sau-es.netlify.app/).

## 📝 About

- SauES is a custom encryption standard inspired mainly by the DES standard. It is a symmetric key encryption standard.

## 💡Motivation

- The main motivation behind this project was to learn how cryptography and encryption standards work under the hood.

## 🧪 Specifications

<table>
    <tr>
        <th>Rounds</th>
        <td>6</td>
    </tr>
    <tr>
        <th>Block Size</th>
        <td>48 bits</td>
    </tr>
    <tr>
        <th>Key Size</th>
        <td>48 bits</td>
    </tr>
    <tr>
        <th>Key Space</th>
        <td>2<sup>48</sup> keys</td>
    </tr>
</table>

## 🪄 Algorithm

- The key is initially permuted using a permutation table, and left shifted in each round(6).
- The block is permuted using a permutation table in each round(6).

![Encryption](https://cdn.discordapp.com/attachments/1180115919482130464/1183487211920949318/image.png?ex=6588835b&is=65760e5b&hm=d61f5abdecbee5ee5eba0b123591ca6614b43abd7b70f2a1e9b38940174ba473&)

![Key Generation](https://cdn.discordapp.com/attachments/1180115919482130464/1183479915081891941/image.png?ex=65887c8f&is=6576078f&hm=c66598fa8fd41f885e16dd87191b4c56a2f579fd39e8e7b09a843a3a1d7c86fa&)

## 🧱 Built With

- ![React](https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB)
- ![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-38B2AC?style=for-the-badge&logo=tailwind-css&logoColor=white)
- ![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)
- ![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)

## ⚙️ Installation and setup instructions

1. Clone down this repo. Use Git or checkout with SVN using the web URL <br><br>
   ```sh
   git clone https://github.com/bedre7/SauES.git
   ```
2. Change directory to the cloned repo<br><br>
   ```sh
   cd SauES
   ```
3. Create .env file under frontend directory and add the following line<br><br>
   ```sh
   VITE_API_URL=http://localhost:5000
   ```
4. Install python dependencies in backend directory<br><br>
   ```sh
   cd backend && pip install -r requrements.txt
   ```
5. Install npm dependencies in frontend directory<br><br>
   ```sh
   cd frontend && npm install
   ```
6. Start both frontend and backend development servers <br><br>
   1. frontend<br><br>
      ```sh
      cd frontend && npm start
      ```
   2. backend<br><br>
      ```sh
      cd backend && python app.py
      ```
