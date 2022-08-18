import React from 'react';
import Footer from "../components/Footer";

export default class NoteViewer extends React.Component {
  constructor () {
    super();

    this.state = {
      note: window.location.pathname.replace('/notes/', '').replace('/', ''),
      title: '',
      pages: [],
    };
  }

  componentDidMount() {
    fetch(`${process.env.REACT_APP_API_URL}/notes/${this.state.note}/`)
      .then(response => response.json())
      .then(data => this.setState({
        title: data.title,
        pages: data.pages,
      }))
      .catch(error => console.error(error));
  }

  render() {
    return (
      <main>
        <h2>{this.state.title}</h2>
        <section>
          {
            this.state.pages.map((page, index, pages) => {
              let delimiter = (index < pages.length - 1) ? <hr /> : '';

              return (
                <div key={page}>
                  <img className="page" src={page} alt="Page" />
                  {delimiter}
                </div>
              );
            })
          }
        </section>
        <Footer />
      </main>
    );
  }
}
