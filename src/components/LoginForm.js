import React from 'react';

export default class EmailForm extends React.Component {
  constructor(props) {
    super(props);
    this.state = {email: ''};

    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleChange(event) {
    this.setState({email: event.target.value});
  }

  handleSubmit(event) {
    fetch(
      process.env.REACT_APP_API_URL + '/mail',
      {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({'email': this.state.email}),
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
            value={this.state.email}
            maxLength="254"
            placeholder="mail@example.com"
            onChange={this.handleChange}
          />
          <input
            type="password"
            name="password"
            maxLength="128"
            placeholder="********"
          />
          <input type="submit" value="Log in" />
        </form>
      </main>
    );
  }
}
