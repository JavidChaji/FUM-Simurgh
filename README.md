<a name="readme-top"></a>

[![Contributors][Contributors-Shield]][Contributors-URL]
[![Forks][Forks-Shield]][Forks-URL]
[![Stargazers][Stars-Shield]][Stars-URL]
[![Issues][Issues-Shield]][Issues-URL]
[![MIT License][License-Shield]][License-URL]

[![LinkedIn][LinkedIn-Shield]][LinkedIn-URL]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/JavidChaji/FUM-Simurgh">
    <img src="Images/Simurgh_White_Background.svg" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Simurgh</h3>

  <p align="center">
    Your Educational Chatbot for Ferdowsi University of Mashhad
    <br />
    <a href="https://github.com/JavidChaji/FUM-Simurgh"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/JavidChaji/FUM-Simurgh">View Demo</a>
    ·
    <a href="https://github.com/JavidChaji/FUM-Simurgh/issues">Report Bug</a>
    ·
    <a href="https://github.com/JavidChaji/FUM-Simurgh/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Screen Shot][Product-Screenshot]][Product-URL]

Simurgh is your intelligent chatbot companion designed to assist Ferdowsi University of Mashhad students in finding answers to their educational and administrative queries. With Simurgh's help, navigating the university's academic landscape becomes effortless. Whether you're seeking course information, registration guidance, or campus resources, Simurgh is your trusted ally on the path to academic success.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

Technologies and Tools Utilized in this Project

* [![Python][Python-Shield]][Python-URL]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

### Prerequisites

<details>
  <summary><h4> Rocket.Chat Prerequisites </h4></summary>


* npm
  ```sh
  npm install npm@latest -g
  ```

1. You must have node version 14

    - Check the Node version and make sure it's 14
      ```sh
      node -v
      ```

    - If your node version was not 14
      ```sh
      sudo n 14.21.3
      ```

2. you must have meteor

    - install meteor
      ```sh
      npm install -g meteor
      ```

    - If having problem with installing
      ```sh
      curl https://install.meteor.com/\?release\=2.13.3 | sh
      sudo npm install -g meteor --unsafe-perm
      ```

3. install yarn

    - Install yarn for arch linux
      ```sh
      sudo npm install --global yarn 
      sudo pacman -S yarn
      ```

4. Clone the repo
    - Clone this repo: `git clone https://github.com/JavidChaji/FUM-Simurgh.git`
  
5. Run `yarn` to install dependencies



6. **Starting Rocket.Chat:**

    ```sh
    yarn dev # run all packages
    ```
    OR
    ```sh
    yarn dsv # run only meteor (front and back) with pre-built packages
    ```

---
</details>

<details>
  <summary><h4> Rasa Prerequisites </h4></summary>

<em>
> [!WARNING]  
> PYTHON3 SUPPORTED VERSIONS
> 
> Currently, rasa supports the following Python versions: 3.7, 3.8, 3.9 and 3.10. Note that Python 3.10 is only supported for versions 3.4.x and upwards. Additionally, rasa installation on Apple Silicon with Python 3.10 is not functional in 3.4.x but will be supported starting from 3.5.x.
</em>

these steps are for linux

1. So We Install Python Version 3.10 in the virtual environment

    ```sh
    python3.10 -m venv .venv
    ```
    
    - we can move to the virtual environment by:

        ```sh
        source .venv/bin/activate
        ```

    - after moving to virtual environment we check if our python version are correct

        ```sh
        python -V
        ```

    - and also make sure pip is installed

        ```sh
        pip -V
        ```

    - Install Rasa and Upgrade pip (it's may take a while)

        ```sh
        python -m pip install --upgrade pip rasa
        ```

    - so to see switches of rasa we can use

        ```sh
        python -m rasa --help
        ```
    - to initiate ower rasa project we use this command (rasa will be asking you some questions and then you should be fine)

        ```sh
        python -m rasa --init
        ```
</details>

<details>
  <summary><h4> Rasa and Rocket.Chat Connection </h4></summary>
  
### 2. Rocket.Chat Bot User Configurations

Create a Rasa bot user in Rocket.Chat. You can either manually login to Rocket.Chat and create a bot user via the 
user management page or can use the following script to create the bot user.

Run the following command to create the RASA bot.

**Note:** Please replace the user name and password of the RocketChat admin and bot user accordingly. 
```sh
python3 scripts/bot_config.py -an admin_username -ap admin_password -bn bot_username -bp bot_pass -r http://rocketchaturl
```

If you are using docker-compose following is a sample usage

```sh
python3 scripts/bot_config.py -an admin -ap admin -bn bot_rasa -bp bot_rasa -r http://localhost:3000
```

### 3. Configure Rasa Bot

* Configure the Credentials file

    Update your `credentials.yml` file inside the `bot_rasa` folder with Rasa bot's username and password.
    ```sh
    rocketchat:
      user: "bot_rasa"
      password: "bot_rasa"
      server_url: "http://localhost:3000"
    ```

* Train the Machine Learning Model
    The Rasa bots machine learning model can built by using either Rasa CLI or Docker. After the training a machine 
    learning model will be created inside the `bot_rasa/models` folder.
    
    * **If using Docker**
        
        ```sh
        docker run -it -v $(pwd)/bot_rasa:/app rasa/rasa train
        ```
    
    * **If using Rasa CLI**
    
        ```bash
        pip3 install rasa
        cd bot_rasa
        rasa train
        ``` 
    
### 4. Start Rasa server

Rasa bot can be started via the Docker or Rasa CLI. 

* **If using Docker-compose**

    ```sh
    docker-compose up -d bot_rasa
    ```

* **If using Rasa CLI**

    ```python
    cd bot_rasa
    rasa run --enable-api --debug
    ```

#### 5. Make Rasa Bot accessible by Rocket.Chat

The Rasa bot should be reachable via Rocket.Chat.

*  If you are following the tutorial with docker-compose file then following is the URL to access the Rasa bot.
    ```bash
    http://bot_rasa:5005
    ```
    

* If you are trying to connect to a standalone Rocket.Chat instance or using Rasa CLI, lets user ngrok to get a 
public url for the Rasa Bot. (or just use localhost:5005)

    Install ngrok via: https://ngrok.com/download

    After downloading the ngrok navigate to the ngrok file in the downloded content and execute the following command. 
    This will provide a public URL to the Rasa bot

    ```bash
    ./ngork http 5005
    ```
    
    Following will be the output of ngrok
    ```sh                                                                                                                                                                                                      
    Session Status                online                                                                                                                                                                        
    Session Expires               7 hours, 59 minutes                                                                                                                                                           
    Version                       2.3.30                                                                                                                                                                        
    Region                        United States (us)                                                                                                                                                            
    Web Interface                 http://127.0.0.1:4040                                                                                                                                                         
    Forwarding                    http://e3d5a17b.ngrok.io -> http://localhost:5005                                                                                                                             
    Forwarding                    https://e3d5a17b.ngrok.io -> http://localhost:5005  
    ```
    Copy the http URL provided by ngrok: `http://e3d5a17b.ngrok.io`

### 6. Configure Rocket.Chat webhook

Go to **Administration > New Integration > Outgoing webhook**.
Inside the configuration insert this:

```
Event Trigger: Message Sent
Enabled: True
Channel: #general
URLs: http://bot_rasa:5005/webhooks/rocketchat/webhook
Post as: bot_rasa
```

If you are using ngrok then replace the URL `http://bot:5005`, with the url obtained by ngrok.

```bash
URLs: http://ngrok_public_url/webhooks/rocketchat/webhook
```

**Save** all the changes.

### Example

Type `@bot_rasa hello` to start a conversation with the Rasa bot
![example]

[example]: Images/rasa_bot_example.png


### Additional Information

If you want the Rasa bot to direct message with the users create another webhook with the following configurations

```
Event Trigger: Message Sent
Enabled: True
Channel: all_direct_messages
URLs: http://bot_rasa:5005/webhooks/rocketchat/webhook
Post as: bot_rasa
```
</details>

        
### Installation



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Javid Chaji - [@JavidChaji](https://twitter.com/JavidChaji) - javid.chaji@gmail.com

Project Link: [FUM-Simurgh](https://github.com/JavidChaji/FUM-Simurgh)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

Use this space to list resources you find helpful and would like to give credit to. I've included a few of my favorites to kick things off!

* [Choose an Open Source License](https://choosealicense.com)
* [GitHub Emoji Cheat Sheet](https://www.webpagefx.com/tools/emoji-cheat-sheet)
* [Malven's Flexbox Cheatsheet](https://flexbox.malven.co/)
* [Malven's Grid Cheatsheet](https://grid.malven.co/)
* [Img Shields](https://shields.io)
* [GitHub Pages](https://pages.github.com)
* [Font Awesome](https://fontawesome.com)
* [React Icons](https://react-icons.github.io/react-icons/search)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

<!-- Contributors -->
[Contributors-Shield]: https://img.shields.io/github/contributors/JavidChaji/FUM-Simurgh.svg?style=for-the-badge

[Contributors-URL]: https://github.com/JavidChaji/FUM-Simurgh/graphs/contributors


<!-- Forks -->
[Forks-Shield]: https://img.shields.io/github/forks/JavidChaji/FUM-Simurgh.svg?style=for-the-badge

[Forks-URL]: https://github.com/JavidChaji/FUM-Simurgh/network/members


<!-- Stars -->
[Stars-Shield]: https://img.shields.io/github/stars/JavidChaji/FUM-Simurgh.svg?style=for-the-badge

[Stars-URL]: https://github.com/JavidChaji/FUM-Simurgh/stargazers


<!-- Issues -->
[Issues-Shield]: https://img.shields.io/github/issues/JavidChaji/FUM-Simurgh.svg?style=for-the-badge

[Issues-URL]: https://github.com/JavidChaji/FUM-Simurgh/issues


<!-- License -->
[License-Shield]: https://img.shields.io/github/license/JavidChaji/FUM-Simurgh.svg?style=for-the-badge

[License-URL]: https://github.com/JavidChaji/FUM-Simurgh/blob/master/LICENSE.txt


<!-- LinkedIn -->
[LinkedIn-Shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555

[LinkedIn-URL]: https://linkedin.com/in/JavidChaji


<!-- Python -->
[Python-Shield]: https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue

[Python-URL]: https://nextjs.org/


<!-- Product -->
[Product-Screenshot]: Images/Screenshot.png

[Product-URL]: .
