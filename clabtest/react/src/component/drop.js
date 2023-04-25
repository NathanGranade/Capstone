import React from 'react';
import jsPDF from 'jspdf';


class Drop extends React.Component {
  constructor(props) {
    super(props);

    this.state = {
      tab: '',
      fetchedData: null, // initialize the fetchedData
      fileName: '',
      pdfTitle: '',
    };

    this.handleUpload = this.handleUpload.bind(this);
    this.handleTitleChange = this.handleTitleChange.bind(this);
    
  }

  handleTitleChange(event) {
    this.setState({ pdfTitle: event.target.value });
  }

  handleUpload(event) {
    event.preventDefault();
    

    const data = new FormData();
    const uploadedFile = this.uploadInput.files[0];
    data.append('file', uploadedFile);
    this.setState({ fileName: uploadedFile.name.split('.')[0] }); // set the file name

    fetch('http://localhost:8000/upload', {
      method: 'POST',
      body: data,
    }).then((response) => {
      response.json().then((body) => {
        console.log(body);
        this.setState({ fetchedData: body }); // set the state with the data from /upload
      });
    });
    document.getElementById("pdfTitle").value = ""
    document.getElementById("SavePDF").disabled = false
  }

  generatePDF() {
    const { fetchedData, fileName, pdfTitle } = this.state;
    document.getElementById("SavePDF").disabled = true
    const pdfContent = fetchedData.tab;
    const pdf = new jsPDF();
    const pageWidth = pdf.internal.pageSize.getWidth();
    const pageHeight = pdf.internal.pageSize.getHeight();
  
    // Set font to monospace (courier)
    pdf.setFont('courier');
  
    // Add title and center it
    pdf.setFontSize(14);
    const titleWidth = pdf.getStringUnitWidth(pdfTitle) * pdf.getFontSize() / pdf.internal.scaleFactor;
    const titleXPosition = (pageWidth - titleWidth) / 2;
    pdf.text(pdfTitle, titleXPosition, 20);
  
    // Add content below the title
    pdf.setFontSize(10);
    const scores = pdfContent.split('\n\n');
    let yPosition = 30;
    let xPosition = 10;
    let column = 0;
  
    scores.forEach((score) => {
      const scoreLines = score.split('\n');
      const maxLineWidth = Math.max(...scoreLines.map(line => pdf.getStringUnitWidth(line) * pdf.getFontSize() / pdf.internal.scaleFactor));
      const scoreWidth = maxLineWidth;
  
      if (column === 1 && xPosition + scoreWidth > pageWidth - 10) {
        column = 0;
        yPosition += 30;
        xPosition = 10;
      }
  
      if (yPosition + 30 > pageHeight - 10) {
        pdf.addPage();
        yPosition = 30; // Reset the yPosition for the new page
      }
  
      pdf.text(score, xPosition, yPosition);
  
      if (column === 0 && xPosition + scoreWidth <= pageWidth / 2) {
        column += 1;
        xPosition = pageWidth / 2;
      } else {
        column = 0;
        yPosition += 30;
        xPosition = 10;
      }
    });
  
    pdf.save(`${fileName}.pdf`);
  }

  render() {
    const { fetchedData } = this.state;
  
    return (
      <body>
        <div id="upload">
          <h1>Choose a file to upload</h1>
          <form id="choose file" onSubmit={this.handleUpload}>
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
              {/* Title input */}
              <label htmlFor="pdfTitle">PDF Title:</label>
              <input
                type="text"
                id="pdfTitle"
                name="pdfTitle"
                onChange={this.handleTitleChange}
              />
              {/* Save as PDF button */}
              <button id="SavePDF" onClick={() => this.generatePDF()}>Save as PDF</button>
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