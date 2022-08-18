import React from 'react';
import Footer from "../components/Footer";

export default class NoteViewer extends React.Component {
  constructor () {
    super();

    this.state = {
      pages: [],
    };
  }

  componentDidMount() {
    this.setState({
      pages: [
        'https://dmitrvk.ml/public/notes/python/pages/python-0.png',
        'https://dmitrvk.ml/public/notes/python/pages/python-1.png',
        'https://dmitrvk.ml/public/notes/python/pages/python-2.png',
        'https://dmitrvk.ml/public/notes/python/pages/python-3.png',
      ],
    })
  }

  render() {
    return (
      <main>
        <section>
          {
            this.state.pages.map(page => {
              return (
                <div>
                  <img className="page" src={page} alt="Page" />
                  <hr />
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
