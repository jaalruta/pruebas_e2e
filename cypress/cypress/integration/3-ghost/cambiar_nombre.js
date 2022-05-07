describe ('crear', function(){
    it ('login', function(){
        cy.visit("http://localhost:2368/ghost/#/signin");
        cy.get('#ember7').type('j.otalvaro@uniandes.edu.co');
        cy.get('#ember9').type('irchete7811');
        cy.get('#ember11 > span').click();
        cy.wait(1000);
        cy.get(".gh-nav-body a[href='#/settings/']").click();
        cy.wait(1000);
        cy.get(".view-container a[href='#/settings/general/']").click();
        cy.get(':nth-child(2) > .gh-expandable > :nth-child(1) > .gh-expandable-header > .gh-btn > span').click();
        cy.get('#ember100').type(' MISO');
        cy.get('#ember68 > span').click();
    })
})