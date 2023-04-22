import React from 'react';

function Home() {
  return (
    <main>
      <header className="title-body">
        <a href="/" id="title">
          <h1 className="title">CLAB🎵</h1>
        </a>
        <a href="drop">
          <button className="button-19">Get Started</button>
        </a>
        <p className="title-text">Create Sheet Music with Ease</p>
      </header>
      <section className="title-body" id="about">
        <article className="about-section">
          <h2>What is CLAB?🤔</h2>
          <hr />
          <p>CLAB, which is short for collab, is a music songwriting tool designed to make it easier for musicians and musicologists to learn, transcribe, and create music notation. This innovative tool employs artificial intelligence algorithms to detect notes and rhythms in audio files. By using CLAB, users can create and store music notation with the click of a button. CLAB is an ideal tool for those looking to streamline the process of creating music notation from audio recordings.</p>
        </article>
        <article className="about-section">
          <h2>Who is CLAB for?👨‍💼</h2>
          <hr />
          <p>CLAB is an excellent tool for anyone looking to simplify the process of creating music notation. It is targeted towards professionals in the music industry, such as composers, arrangers, and musicologists, as well as intermediate musicians who are looking for an easy way to create music notation from audio recordings. This is our target audience, but with a bit of learning, CLAB can be useful to anyone! CLAB is particularly useful for those who work with audio files and want to transcribe them into written music.</p>
        </article>
        <article className="about-section">
          <h2>How does CLAB work?👩‍💻</h2>
          <hr />
          <p>CLAB is an excellent tool for anyone looking to simplify the process of creating music notation. It is targeted towards professionals in the music industry, such as composers, arrangers, and musicologists, as well as intermediate musicians who are looking for an easy way to create music notation from audio recordings. This is our target audience, but with a bit of learning, CLAB can be useful to anyone! CLAB is particularly useful for those who work with audio files and want to transcribe them into written music.</p>
        </article>
      </section>
      <section className="title-body" id="contact">
        <h1>Contact Us!</h1>
        <form>
          <p>
            Email{' '}
            <input
              id="email"
              type="text"
              name="email"
              placeholder="email"
            />
          </p>
          <p>
            Name{' '}
            <input
              id="username"
              type="text"
              name="username"
              placeholder="name"
            />
          </p>
          <p>
            <textarea
              className="message"
              type="text"
              name="password"
              placeholder="Message..."
            ></textarea>
          </p>
          <div className="controls" id="b1">
            <input className="button-19" id="submit" type="submit" />
          </div>
        </form>
      </section>
    </main>
  );
}

export default Home;
