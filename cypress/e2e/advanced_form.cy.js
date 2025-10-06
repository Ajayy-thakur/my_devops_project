describe('Advanced Form Interaction Test', () => {
  it('Handles inputs, dropdowns, checkboxes, and buttons', () => {
    // Demo page
    cy.visit('https://example.cypress.io/commands/actions')

    // Text input
    cy.get('.action-email')
      .type('ajay@example.com')
      .should('have.value', 'ajay@example.com')

    // Another input
    cy.get('.action-password')
      .type('123456')
      .should('have.value', '123456')

    // Checkbox
    cy.get('.action-checkboxes [type="checkbox"]').check().should('be.checked')

    // Radio button
    cy.get('.action-radios [type="radio"]').first().check().should('be.checked')

    // Dropdown select
    cy.get('.action-select')
      .select('apples')
      .should('have.value', 'apples')

    // Button click
    cy.get('.action-btn')
      .contains('Click to toggle')
      .click()
      .should('exist')
  })
})

