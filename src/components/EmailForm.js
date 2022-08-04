import React from 'react';

export default class EmailForm extends React.Component {
  constructor(props) {
    super(props);
    this.state = {value: ''};

    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleChange(event) {
    this.setState({value: event.target.value});
  }

  handleSubmit(event) {
    fetch(
      process.env.REACT_APP_API_URL + '/mail',
      {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({'email': this.state.value}),
      },
    );

    event.preventDefault();
  }

  render() {
    return (
      <main>
        <form onSubmit={this.handleSubmit}>
          <input
            type="email"
            name="email"
            value={this.state.value}
            placeholder="mail@example.com"
            onChange={this.handleChange}
          />
          <input type="submit" value="Send mail" />
        </form>
      </main>
    );
  }
}
