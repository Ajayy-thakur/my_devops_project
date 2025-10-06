describe('Buttons and Form Interaction Test', () => {
  it('Fills input, clicks button, and checks output', () => {
    // Demo page
    cy.visit('https://example.cypress.io/commands/actions')

    // Type in input box
    cy.get('.action-email')
      .type('ajay@example.com')
      .should('have.value', 'ajay@example.com')

    // Click a button
    cy.get('.action-btn')
      .contains('Click to toggle')
      .click()

    // Check if a new element appears
    cy.get('.action-btn')
      .contains('Click to toggle')
      .should('exist')
  })
})

