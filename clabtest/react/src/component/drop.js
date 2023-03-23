import React from 'react';
import Display from './display.js';

class Drop extends React.Component {
  constructor(props) {
    super(props);

    this.state = {
      tab: '',
    };

    this.handleUpload = this.handleUpload.bind(this);
    this.handleScroll = this.handleScroll.bind(this);
  }

  handleUpload() {

    const data = new FormData();
    data.append('file', this.uploadInput.files[0]);

    fetch('http://localhost:8000/upload', {
      method: 'POST',
      body: data,
    }).then((response) => {
      response.json().then((body) => {
        console.log(response);
      });
    });
  }
  handleScroll(){
    const element = document.getElementById('');
    if(element){
      element.scrollIntoView({behavior: 'smooth'});
    }

  };
  render() {
    return (
      <body>
      <div id="upload">
      <h1>Choose a file to upload</h1>
      <form onSubmit={this.handleUpload}>
        <div>
          <input ref={(ref) => { this.uploadInput = ref; }} type="file" />
        </div>
        <br />
        <div>
          <button className="btn-scroll" onClick={this.handleScroll}>Upload</button>
        </div>
      </form>
      <Display />
      </div>
      </body>
    );

  }
}

export default Drop;