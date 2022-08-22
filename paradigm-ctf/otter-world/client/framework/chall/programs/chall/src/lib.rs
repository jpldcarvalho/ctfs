use anchor_lang::prelude::*;
use anchor_spl::token::{Mint, Token, TokenAccount, Transfer};
use anchor_spl::token;

pub use anchor_lang;
pub use anchor_spl;

pub const FLAG_SEED: &[u8] = b"flag";

declare_id!("osecio1111111111111111111111111111111111112");

#[program]
pub mod chall {
    use super::*;

    pub fn get_flag(_ctx: Context<GetFlag>, magic: u64) -> Result<()> {
        // 8A56287 = 145056391
        assert!(magic == 0x1337 * 0x7331);

        Ok(())
    }

}

#[derive(Accounts)]
pub struct GetFlag<'info> {
    #[account(
        init,
        seeds = [ FLAG_SEED ],
        bump,
        payer = payer,
        space = 1000
    )]
    pub flag: Account<'info, Flag>,

    #[account(mut)]
    pub payer: Signer<'info>,
    pub system_program: Program<'info, System>,
    pub rent: Sysvar<'info, Rent>,
}


#[account]
#[repr(C, align(8))]
#[derive(Default)]
pub struct Flag {
}
