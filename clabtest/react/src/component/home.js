
import React from 'react';
  
function Home (){
    return (
    <body>
        <div className="title-body">
        <a href="/" id ="title"><h1 className="title">CLAB🎵</h1></a>
            <a href="drop"><button className="button-19" id="Start">Get Started</button></a>
            <p className="title-text">Create Sheet Music with Ease</p>
        </div>
        <div className="title-body" id="about">
        <div class="about-section">
            <h2>What is CLAB?🤔</h2>
            <hr></hr>
            <p>CLAB, which is short for collab, is a music songwriting tool designed to make it easier for musicians and musicologists to learn, transcribe, and create music notation. This innovative tool employs artificial intelligence algorithms to detect notes and rhythms in audio files. By using CLAB, users can create and store music notation with the click of a button. CLAB is an ideal tool for those looking to streamline the process of creating music notation from audio recordings.</p>
        </div>
        <div class="about-section">
            <h2>Who is CLAB for?👨‍💼</h2>
            <hr></hr>
            <p>CLAB is an excellent tool for anyone looking to simplify the process of creating music notation. It is targeted towards professionals in the music industry, such as composers, arrangers, and musicologists, as well as intermediate musicians who are looking for an easy way to create music notation from audio recordings. This is our target audience, but with a bit of learning, CLAB can be useful to anyone! CLAB is particularly useful for those who work with audio files and want to transcribe them into written music.</p>
        </div>
        <div class="about-section">
            <h2>How does CLAB work?👩‍💻</h2>
            <hr></hr>
            <p>CLAB employ artificial intelligence algorithms to detect notes and rhythms in audio files. The software analyzes the audio file and uses machine learning techniques to identify each note and the timing of each note. Once the software has identified the notes and rhythms, it creates a music notation file that the user can edit, store, and share. The user can export the music notation file in a PDF format. CLAB is easy to use and provides accurate results, making it an indispensable tool for anyone looking to accelerate the process of creating music notation.</p>
        </div>
        </div>
        <div class="title-body" id="contact">
                <h1>Contact Us!</h1>
                <p>Email <input id="email" type = "text" name = "email" placeholder="email"/></p>
                <p>Name <input id="username" type = "text" name = "username" placeholder="name"/></p>
                <p><textarea class="message" type = "text" name = "password" placeholder="Message..."></textarea></p>
                <div class="controls" id="b1"><input class="button-19" id="submit" type = "submit"/></div>
        </div>
    </body>
    )
}
  
export default Home;