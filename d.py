@bot.command()
async def redeem(ctx, license_key: str):
    try:
        if any(key == license_key for key in redeemed_users.values()):
            embed = create_embed(
                "License Key Already Redeemed",
                "This license key has already been redeemed by another user.",
                color=0xff0000
            )
            await ctx.send(embed=embed)
            return

        keyauthapp.license(license_key)
        redeemed_users[ctx.author.id] = license_key
        save_redeemed_keys(redeemed_users)
        
        # Assign role to user
        role_name = "Customers"  # Change this to the role you want to assign
        role = discord.utils.get(ctx.guild.roles, name=role_name)
        if role:
            await ctx.author.add_roles(role)
            embed = create_embed(
                "License Redeemed Successfully",
                f"You have successfully redeemed your license key! The '{role_name}' role has been assigned to you."
            )
        else:
            embed = create_embed(
                "License Redeemed Successfully",
                f"You have successfully redeemed your license key! However, the role '{role_name}' was not found.",
                color=0xff0000
            )
        
        await ctx.send(embed=embed)
        
    except KeyAuthException as e:
        embed = create_embed(
            "Error Redeeming License",
            f"An error occurred while redeeming the license: {str(e)}",
            color=0xff0000
        )
        await ctx.send(embed=embed)
    except Exception as e:
        embed = create_embed(
            "Error Redeeming License",
            f"An error occurred while redeeming the license: {str(e)}",
            color=0xff0000
        )
        await ctx.send(embed=embed)
