describe('Demo Page Test', () => {
  it('Types in an input box', () => {
    cy.visit('https://example.cypress.io/commands/actions')
    cy.get('.action-email').type('test@example.com')
      .should('have.value', 'test@example.com')
  })
})

