import React from 'react';

class Drop extends React.Component {
  constructor(props) {
    super(props);

    this.state = {
      tab: '',
      fetchedData: null, // initialize the fetchedData
    };

    this.handleUpload = this.handleUpload.bind(this);
    
  }

  handleUpload(event) {
    event.preventDefault();

    const data = new FormData();
    data.append('file', this.uploadInput.files[0]);

    console.log(data);
    fetch('http://localhost:8000/upload', {
      method: 'POST',
      body: data,
    }).then((response) => {
      response.json().then((body) => {
        this.setState({ fetchedData: body }); // set the state with the data from /upload
      });
    });
  }

  render() {
    const { fetchedData } = this.state;
  
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
              <button className="button-19" id="Upload">Upload</button>
            </div>
          </form>
          {/* Display fetched data */}
          {fetchedData ? (
            <div className="tab">
              {/* Display JSON data */}
              <p>
              {fetchedData.tab}
              </p>
            </div>
          ) : null}
        </div>
      </body>
    );
  }
}

export default Drop;