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
              let url = `/notes/${note.name}`;
              let thumbnail_url = `https://dmitrvk.ml/public/notes/${note.name}/${note.name}-thumbnail.png`;

              return (
                <Note
                  key={note.name}
                  name={note.name}
                  url={url}
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
      <a className="note" href={this.props.url}>
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
