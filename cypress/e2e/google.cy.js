describe('Google Search Test', () => {
  it('searches for Selenium', () => {
    cy.visit('https://www.google.com')
    cy.get('input[name="q"]').type('Selenium{enter}')
    cy.title().should('include', 'Selenium')
  })
})

