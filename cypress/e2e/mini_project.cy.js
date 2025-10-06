describe('Mini Cypress Project: Multi-page navigation', () => {
  it('Visits pages, fills forms, clicks buttons, and checks content', () => {
    // Page 1: Actions demo
    cy.visit('https://example.cypress.io/commands/actions')
    cy.get('.action-email').type('ajay@example.com').should('have.value', 'ajay@example.com')
    cy.get('.action-btn').contains('Click to toggle').click()

    // Page 2: Navigation demo
    cy.visit('https://example.cypress.io/commands/navigation')
    cy.url().should('include', '/navigation')
    cy.get('.home-link').contains('cy.visit()').click()
    cy.url().should('include', '/commands/actions')

    // Page 3: Assertions demo
    cy.visit('https://example.cypress.io/commands/assertions')
    cy.get('.assertion-table').should('exist')
    cy.get('.assertion-table td').first().should('contain.text', '1')

    // Checkbox / Radio interaction
    cy.visit('https://example.cypress.io/commands/actions')
    cy.get('.action-checkboxes [type="checkbox"]').check().should('be.checked')
    cy.get('.action-radios [type="radio"]').first().check().should('be.checked')
  })
})

