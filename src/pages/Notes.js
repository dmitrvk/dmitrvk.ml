import React from 'react';
import Footer from "../components/Footer";

export default class Notes extends React.Component {
  constructor () {
    super();

    this.state = {
      notes: [],
    };
  }

  componentDidMount() {
    const api_url = 'https://api.github.com/repos/dmitrvk/notes/contents/notes';

    fetch(api_url)
      .then(response => response.json())
      .then(data => this.setState({ notes: data }))
      .catch(error => console.error(error));
  }

  render() {
    return (
      <main>
        <h2>Notes</h2>
        <section id="notes" className="notes">
          {
            this.state.notes.map(note => {
              let pdf_name = note.name.replace('.tex', '.pdf');
              let note_name = pdf_name.replace('.pdf', '');
              let pdf_url = `https://docs.google.com/viewer?url=https://dmitrvk.ml/public/notes/${note_name}/${pdf_name}`;
              let thumbnail_url = `https://dmitrvk.ml/public/notes/${note_name}/${note_name}-thumbnail.png`;

              return (
                <Note
                  key={note_name}
                  name={note_name}
                  pdf_url={pdf_url}
                  thumbnail_url={thumbnail_url}
                />
              );
            })
          }
        </section>
        <Footer />
      </main>
    );
  }
}

class Note extends React.Component {
  render() {
    return (
      <a className="note" href={this.props.pdf_url}>
        <div className="note-inner">
          <img
            className="note-thumbnail"
            src={this.props.thumbnail_url}
            alt={this.props.name}
          />
          <p className="note-caption">{this.props.name}</p>
        </div>
      </a>
    );
  }
}
