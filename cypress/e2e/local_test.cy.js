describe('Local Test Page', () => {
  it('Fills form inputs and clicks submit', () => {
    cy.visit('http://localhost:3000/local_page.html'); // check karo ye URL exact match ho

    cy.get('input[name="firstname"]').type('Ajay');
    cy.get('input[name="lastname"]').type('Thakur');
    cy.get('input[type="submit"]').click();
  });
});


