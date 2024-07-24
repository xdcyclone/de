@bot.command()
async def redeem(ctx, license_key: str):
    try:
        # Check if the license key has already been redeemed
        if any(key == license_key for key in redeemed_users.values()):
            embed = create_embed(
                "License Key Already Redeemed",
                "This license key has already been redeemed by another user.",
                color=0xff0000
            )
            embed.set_footer(text="Made by Cyclone x Hypesharp | discord.gg/shockwavefn")
            await ctx.send(embed=embed)
            return

        # Simulate redeeming the license key with KeyAuth
        # Replace with actual logic using KeyAuth API
        # Assuming keyauthapp.license(license_key) returns a dictionary with user data or raises an exception on invalid keys
        try:
            keyauthapp.license(license_key)
            redeemed_users[ctx.author.id] = license_key
            save_redeemed_keys(redeemed_users)  # Save redeemed keys after updating

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
                    "Role Not Found",
                    f"You have successfully redeemed your license key! However, the role '{role_name}' was not found.",
                    color=0xff0000
                )
        except Exception as e:
            embed = create_embed(
                "Invalid License Key",
                f"The license key '{license_key}' is invalid or expired. Please check the key and try again.",
                color=0xff0000
            )
        
        embed.set_footer(text="Made by Cyclone x Hypesharp | discord.gg/shockwavefn")
        await ctx.send(embed=embed)

    except Exception as e:
        embed = create_embed(
            "Error Redeeming License",
            f"An error occurred while redeeming the license: {str(e)}",
            color=0xff0000
        )
        embed.set_footer(text="Made by Cyclone x Hypesharp | discord.gg/shockwavefn")
        await ctx.send(embed=embed)
