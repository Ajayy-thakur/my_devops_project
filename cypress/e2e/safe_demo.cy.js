describe('Mini Cypress Project: Multi-page safe navigation', () => {
  it('Visits pages and interacts with safe elements', () => {
    // Page 1: Actions demo
    cy.visit('https://example.cypress.io/commands/actions')
    cy.get('.action-email')
      .type('ajay@example.com')
      .should('have.value', 'ajay@example.com')

    cy.get('.action-btn')
      .contains('Click to toggle')
      .click()
      .should('exist')

    // Checkbox / Radio interaction
    cy.get('.action-checkboxes [type="checkbox"]')
      .check()
      .should('be.checked')

    cy.get('.action-radios [type="radio"]')
      .first()
      .check()
      .should('be.checked')
  })
})

