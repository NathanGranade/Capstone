import React from 'react';

class Drop extends React.Component {
  constructor(props) {
    super(props);

    this.state = {
      tab: '',
    };

    this.handleUpload = this.handleUpload.bind(this);
  }

  handleUpload(ev) {
    ev.preventDefault();

    const data = new FormData();
    data.append('file', this.uploadInput.files[0]);

    fetch('http://localhost:8000/upload', {
      method: 'POST',
      body: data,
    }).then((response) => {
      response.json().then((body) => {
        this.setState({ tab: `http://localhost:8000/${body.file}` });
        console.log(data)
      });
    });
  }

  render() {
    return (
      <div class="title-body">
      <form onSubmit={this.handleUpload}>
        <div>
          <input ref={(ref) => { this.uploadInput = ref; }} type="file" />
        </div>
        <br />
        <div>
          <button>Upload</button>
        </div>
      </form>
      </div>
    );
  }
}

export default Drop;