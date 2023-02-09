

class Payment {
  constructor(amount) {
    this.amount = amount;
  }
}

class Credit extends Payment {
  constructor(amount, number, expirationDate) {
    super(amount);
    this.number = number;
    this.expirationDate = expirationDate;
  }
}