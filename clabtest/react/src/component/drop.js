import React from 'react';
import Display from './display.js';

class Drop extends React.Component {
  constructor(props) {
    super(props);

    this.state = {
      tab: '',
    };

    this.handleUpload = this.handleUpload.bind(this);
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

  render() {
    return (
      <div className="title-body">
      <form onSubmit={this.handleUpload}>
        <div>
          <input ref={(ref) => { this.uploadInput = ref; }} type="file" />
        </div>
        <br />
        <div>
          <button>Upload</button>
        </div>
      </form>
      <Display />
      </div>
      
    );

  }
}

export default Drop;